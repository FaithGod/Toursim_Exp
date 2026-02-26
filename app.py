<<<<<<< HEAD
import streamlit as st
import pandas as pd
import pickle

# ==========================================================
# Load Models & Data
# ==========================================================

reg_model = pickle.load(open("reg_model.pkl", "rb"))
clf_model = pickle.load(open("clf_model.pkl", "rb"))
popularity_df = pickle.load(open("popularity_df.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

df = pd.read_csv("final_dataset.csv")

# Get exact training feature order
reg_features = reg_model.feature_names_in_
clf_features = clf_model.feature_names_in_

# ==========================================================
# UI
# ==========================================================

st.set_page_config(page_title="Tourism Experience Analytics", layout="wide")
st.title("🌍 Tourism Experience Analytics System")

menu = st.sidebar.selectbox(
    "Select Module",
    ["Predict Rating", "Predict Visit Mode", "Get Recommendations"]
)

# ==========================================================
# 1️⃣ Predict Rating
# ==========================================================

if menu == "Predict Rating":

    st.subheader("📈 Predict Attraction Rating")

    visit_year = st.number_input("Visit Year", 2018, 2025)
    visit_month = st.number_input("Visit Month", 1, 12)

    continent = st.selectbox("Continent", df["Continent"].unique())
    region = st.selectbox("Region", df["Region"].unique())
    country = st.selectbox("Country", df["Country"].unique())
    attraction_type = st.selectbox("Attraction Type", df["AttractionType"].unique())

    if st.button("Predict Rating"):

        # Encode categorical
        continent_enc = encoders["Continent"].transform([continent])[0]
        region_enc = encoders["Region"].transform([region])[0]
        country_enc = encoders["Country"].transform([country])[0]
        attraction_type_enc = encoders["AttractionType"].transform([attraction_type])[0]

        # Create empty input with exact feature order
        input_data = pd.DataFrame(columns=reg_features)

        # Fill required fields
        input_data.loc[0, "UserId"] = 0
        input_data.loc[0, "VisitYear"] = visit_year
        input_data.loc[0, "VisitMonth"] = visit_month
        input_data.loc[0, "AttractionId"] = 0
        input_data.loc[0, "Continent"] = continent_enc
        input_data.loc[0, "Region"] = region_enc
        input_data.loc[0, "Country"] = country_enc
        input_data.loc[0, "UserCity"] = 0
        input_data.loc[0, "AttractionType"] = attraction_type_enc
        input_data.loc[0, "AttractionCity"] = 0

        input_data = input_data.fillna(0)

        prediction = reg_model.predict(input_data)

        st.success(f"⭐ Predicted Rating: {round(prediction[0],2)}")

# ==========================================================
# 2️⃣ Predict Visit Mode
# ==========================================================

elif menu == "Predict Visit Mode":

    st.subheader("🧳 Predict Visit Mode")

    visit_year = st.number_input("Visit Year", 2018, 2025)
    visit_month = st.number_input("Visit Month", 1, 12)

    continent = st.selectbox("Continent", df["Continent"].unique())
    region = st.selectbox("Region", df["Region"].unique())
    country = st.selectbox("Country", df["Country"].unique())
    attraction_type = st.selectbox("Attraction Type", df["AttractionType"].unique())

    if st.button("Predict Visit Mode"):

        continent_enc = encoders["Continent"].transform([continent])[0]
        region_enc = encoders["Region"].transform([region])[0]
        country_enc = encoders["Country"].transform([country])[0]
        attraction_type_enc = encoders["AttractionType"].transform([attraction_type])[0]

        input_data = pd.DataFrame(columns=clf_features)

        input_data.loc[0, "UserId"] = 0
        input_data.loc[0, "VisitYear"] = visit_year
        input_data.loc[0, "VisitMonth"] = visit_month
        input_data.loc[0, "AttractionId"] = 0
        input_data.loc[0, "Rating"] = 0
        input_data.loc[0, "Continent"] = continent_enc
        input_data.loc[0, "Region"] = region_enc
        input_data.loc[0, "Country"] = country_enc
        input_data.loc[0, "UserCity"] = 0
        input_data.loc[0, "AttractionType"] = attraction_type_enc
        input_data.loc[0, "AttractionCity"] = 0

        input_data = input_data.fillna(0)

        prediction = clf_model.predict(input_data)

        st.success(f"🧳 Predicted Visit Mode: {prediction[0]}")

# ==========================================================
# 3️⃣ Recommendation System
# ==========================================================

else:

    st.subheader("🎯 Get Attraction Recommendations")

    user_id = st.number_input(
        "Enter User ID",
        min_value=int(df["UserId"].min()),
        max_value=int(df["UserId"].max())
    )

    if st.button("Recommend Attractions"):

        visited = df[df["UserId"] == user_id]["AttractionId"].unique()
        recommendations = popularity_df[~popularity_df.index.isin(visited)]

        top5 = recommendations.head(5).reset_index()

        attraction_lookup = df[["AttractionId","Attraction"]].drop_duplicates()
        top5 = top5.merge(attraction_lookup, on="AttractionId")

=======
import streamlit as st
import pandas as pd
import pickle

# ==========================================================
# Load Models & Data
# ==========================================================

reg_model = pickle.load(open("reg_model.pkl", "rb"))
clf_model = pickle.load(open("clf_model.pkl", "rb"))
popularity_df = pickle.load(open("popularity_df.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

df = pd.read_csv("final_dataset.csv")

# Get exact training feature order
reg_features = reg_model.feature_names_in_
clf_features = clf_model.feature_names_in_

# ==========================================================
# UI
# ==========================================================

st.set_page_config(page_title="Tourism Experience Analytics", layout="wide")
st.title("🌍 Tourism Experience Analytics System")

menu = st.sidebar.selectbox(
    "Select Module",
    ["Predict Rating", "Predict Visit Mode", "Get Recommendations"]
)

# ==========================================================
# 1️⃣ Predict Rating
# ==========================================================

if menu == "Predict Rating":

    st.subheader("📈 Predict Attraction Rating")

    visit_year = st.number_input("Visit Year", 2018, 2025)
    visit_month = st.number_input("Visit Month", 1, 12)

    continent = st.selectbox("Continent", df["Continent"].unique())
    region = st.selectbox("Region", df["Region"].unique())
    country = st.selectbox("Country", df["Country"].unique())
    attraction_type = st.selectbox("Attraction Type", df["AttractionType"].unique())

    if st.button("Predict Rating"):

        # Encode categorical
        continent_enc = encoders["Continent"].transform([continent])[0]
        region_enc = encoders["Region"].transform([region])[0]
        country_enc = encoders["Country"].transform([country])[0]
        attraction_type_enc = encoders["AttractionType"].transform([attraction_type])[0]

        # Create empty input with exact feature order
        input_data = pd.DataFrame(columns=reg_features)

        # Fill required fields
        input_data.loc[0, "UserId"] = 0
        input_data.loc[0, "VisitYear"] = visit_year
        input_data.loc[0, "VisitMonth"] = visit_month
        input_data.loc[0, "AttractionId"] = 0
        input_data.loc[0, "Continent"] = continent_enc
        input_data.loc[0, "Region"] = region_enc
        input_data.loc[0, "Country"] = country_enc
        input_data.loc[0, "UserCity"] = 0
        input_data.loc[0, "AttractionType"] = attraction_type_enc
        input_data.loc[0, "AttractionCity"] = 0

        input_data = input_data.fillna(0)

        prediction = reg_model.predict(input_data)

        st.success(f"⭐ Predicted Rating: {round(prediction[0],2)}")

# ==========================================================
# 2️⃣ Predict Visit Mode
# ==========================================================

elif menu == "Predict Visit Mode":

    st.subheader("🧳 Predict Visit Mode")

    visit_year = st.number_input("Visit Year", 2018, 2025)
    visit_month = st.number_input("Visit Month", 1, 12)

    continent = st.selectbox("Continent", df["Continent"].unique())
    region = st.selectbox("Region", df["Region"].unique())
    country = st.selectbox("Country", df["Country"].unique())
    attraction_type = st.selectbox("Attraction Type", df["AttractionType"].unique())

    if st.button("Predict Visit Mode"):

        continent_enc = encoders["Continent"].transform([continent])[0]
        region_enc = encoders["Region"].transform([region])[0]
        country_enc = encoders["Country"].transform([country])[0]
        attraction_type_enc = encoders["AttractionType"].transform([attraction_type])[0]

        input_data = pd.DataFrame(columns=clf_features)

        input_data.loc[0, "UserId"] = 0
        input_data.loc[0, "VisitYear"] = visit_year
        input_data.loc[0, "VisitMonth"] = visit_month
        input_data.loc[0, "AttractionId"] = 0
        input_data.loc[0, "Rating"] = 0
        input_data.loc[0, "Continent"] = continent_enc
        input_data.loc[0, "Region"] = region_enc
        input_data.loc[0, "Country"] = country_enc
        input_data.loc[0, "UserCity"] = 0
        input_data.loc[0, "AttractionType"] = attraction_type_enc
        input_data.loc[0, "AttractionCity"] = 0

        input_data = input_data.fillna(0)

        prediction = clf_model.predict(input_data)

        st.success(f"🧳 Predicted Visit Mode: {prediction[0]}")

# ==========================================================
# 3️⃣ Recommendation System
# ==========================================================

else:

    st.subheader("🎯 Get Attraction Recommendations")

    user_id = st.number_input(
        "Enter User ID",
        min_value=int(df["UserId"].min()),
        max_value=int(df["UserId"].max())
    )

    if st.button("Recommend Attractions"):

        visited = df[df["UserId"] == user_id]["AttractionId"].unique()
        recommendations = popularity_df[~popularity_df.index.isin(visited)]

        top5 = recommendations.head(5).reset_index()

        attraction_lookup = df[["AttractionId","Attraction"]].drop_duplicates()
        top5 = top5.merge(attraction_lookup, on="AttractionId")

>>>>>>> e31455d87453c0734c8c0cb351044e5877186c19
        st.write(top5[["Attraction","avg_rating","count"]])