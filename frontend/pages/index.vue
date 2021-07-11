<template>
  <div>
    <div class="bg"></div>
    <h1 class="mainHeading">Find Your Favourite Cuisines</h1>
    <div class="newsStrip">
      <p class="marquee">
        <span class="marqueeSpan">
          <span v-for="ticker of news" :key="ticker._id">
            <img
              src="~/assets/star.svg"
              class="newsStripStart"
              width="15"
              height="15"
            />
            <p>{{ ticker.title }}</p>
          </span>
          <img
            v-if="news.length !== 0"
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
        </span>
      </p>
    </div>
    <div class="searchBar">
      <h3 class="ourMealsHeading">Our Meals</h3>
      <div class="filterContainer">
        <div class="filter" @click="showFilterPanel()">
          <img
            src="~/assets/settings.svg"
            class="searchIcon"
            width="20px"
            height="20px"
          />
        </div>
      </div>
    </div>
    <div class="filterPanel" v-if="isFilterPanelVisible">
      <b-row class="filterPanelRow">
        <b-col cols="2">
          <span class="filterFormInput">Spicy</span>
          <b-form-radio-group
            id="radio-group-2"
            v-model="filterForm.spicy"
            name="radio-sub-component"
          >
            <b-form-radio value="1">1</b-form-radio>
            <b-form-radio value="2">2</b-form-radio>
            <b-form-radio value="3">3</b-form-radio>
          </b-form-radio-group>
        </b-col>
        <b-col cols="2">
          <b-form-checkbox
            class="filterFormInput"
            id="checkbox-1"
            v-model="filterForm.vegan"
            value="true"
            unchecked-value="false"
          >
            Vegan
          </b-form-checkbox>
        </b-col>
        <b-col cols="2">
          <b-form-checkbox
            class="filterFormInput"
            id="checkbox-2"
            v-model="filterForm.vegetarian"
            value="true"
            unchecked-value="false"
          >
            Vegetarian
          </b-form-checkbox>
        </b-col>
        <b-col cols="5">
          <multiselect
            v-model="filterForm.ingredients"
            :options="ingredients"
            :multiple="true"
            :close-on-select="false"
            :taggable="true"
            @tag="addTag"
            tag-placeholder="Add this to search"
            placeholder="Search by Ingredients"
          >
          </multiselect>
        </b-col>
        <b-col cols="1">
          <b-button class="formBtn" type="submit" @click="searchCuisines"
            >Search</b-button
          >
        </b-col>
      </b-row>
      <b-row class="filterPanelRow2">
        <b-col cols="5">
          <b-form-input
            type="text"
            v-model="filterForm.cuisine_name"
            placeholder="Search by cuisine Name"
            trim
            required
          >
          </b-form-input>
        </b-col>
        <b-col cols="3">
          <b-form-input
            type="text"
            v-model="filterForm.country_cuisine"
            placeholder="Search by cuisine country origin"
            trim
            required
          >
          </b-form-input>
        </b-col>
        <b-col cols="3">
          <b-form-input
            type="text"
            v-model="filterForm.time_to_cook"
            placeholder="Search by Time to cook"
            trim
            required
          ></b-form-input>
        </b-col>
        <b-col cols="1">
          <b-button class="formBtnSec" @click="resetSearch()">Reset</b-button>
        </b-col>
      </b-row>
    </div>
    <div class="filterCheckBoxContainer">
      <span class="filterCheckBoxWrap">
        <span
          :class="
            selectedFilter === 'all' ? 'filterCheckBoxActive' : 'filterCheckBox'
          "
          @click="changeFilter('all')"
        >
          <span>All</span>
          <span> ({{ cuisines.length }})</span>
        </span>
      </span>
      <span
        class="filterCheckBoxWrap"
        v-for="filter of filters"
        :key="filter.name"
      >
        <span
          :class="
            selectedFilter === filter.name
              ? 'filterCheckBoxActive'
              : 'filterCheckBox'
          "
          @click="changeFilter(filter.name)"
        >
          <span>{{ filter.name }}</span>
          <span> ({{ filter.length }})</span>
        </span>
      </span>
    </div>
    <p v-if="$fetchState.pending">Fetching cuisines...</p>
    <p v-else-if="$fetchState.error">An error occurred :(</p>
    <div class="recipeContainer" v-else>
      <p v-if="cuisines.length === 0">No Cuisines found</p>
      <div
        class="cardContainer"
        @click="showModal(cuisine)"
        v-for="cuisine of filteredCuisines"
        :key="cuisine._id"
      >
        <img :src="cuisine.cuisine_image" width="100%" height="200px" />
        <div class="cardContent">
          <div class="cardTitleRow">
            <span class="cardTitle">{{ cuisine.cuisine_name }}</span>
            <img
              src="~/assets/heartMarked.svg"
              width="18px"
              class="recipeHeart"
            />
          </div>
          <div class="recipeStars">
            <img
              src="~/assets/star.svg"
              class="recipeStar"
              width="15"
              height="15"
            />
            <img
              src="~/assets/star.svg"
              class="recipeStar"
              width="15"
              height="15"
            />
            <img
              src="~/assets/star.svg"
              class="recipeStar"
              width="15"
              height="15"
            />
            <img
              src="~/assets/star.svg"
              class="recipeStar"
              width="15"
              height="15"
            />
            <img
              src="~/assets/star.svg"
              class="recipeStarOpaque"
              width="15"
              height="15"
            />
            <img
              v-if="cuisine.vegetarian === true"
              src="~/assets/vegetarian.png"
              class="recipeVegan"
              width="30"
              height="30"
              title="Vegetarian"
            />
            <span></span>
            <img
              v-if="cuisine.vegan === true"
              src="~/assets/vegan.jpeg"
              class="recipeStar"
              width="30"
              height="30"
              title="Vegan"
            />
            <img
              v-if="
                cuisine.spicy === '1' ||
                  cuisine.spicy === '2' ||
                  cuisine.spicy === '3'
              "
              src="~/assets/spicy.jpeg"
              class="recipeStar"
              width="30"
              height="30"
              title="Spicy-1"
            />
            <img
              v-if="cuisine.spicy === '3' || cuisine.spicy === '2'"
              src="~/assets/spicy.jpeg"
              class="recipeStar"
              width="30"
              height="30"
              title="Spicy-2"
            />
            <img
              v-if="cuisine.spicy === '3'"
              src="~/assets/spicy.jpeg"
              class="recipeStar"
              width="30"
              height="30"
              title="Spicy-3"
            />
          </div>
          <div class="cardTitleRow">
            <div class="recipeTagsContainer">
              <span
                class="recipeTag"
                v-for="country of cuisine.country_cuisine"
                :key="cuisine._id + country"
              >
                <span>{{ country }}</span>
              </span>
            </div>
            <div class="recipeTime">
              <span>we</span> {{ cuisine.time_to_cook }} mins
            </div>
          </div>
        </div>
      </div>
    </div>
    <b-modal id="cuisine-modal" :title="modalData.cuisine_name" size="lg">
      <div class="cardTitleRowModal">
        <img :src="modalData.cuisine_image" />
        <h3>Ingredients</h3>
        <div class="recipeTagsContainerModal">
          <span
            class="recipeTag"
            v-for="(ingredient, index) of modalData.ingredients"
            :key="index"
          >
            <span>{{ ingredient.original_string }}</span>
          </span>
        </div>
      </div>
    </b-modal>
  </div>
</template>
<script lang="ts">
import Multiselect from "vue-multiselect";
export default {
  components: { Multiselect },
  layout: "header",
  data() {
    return {
      cuisines: [],
      filteredCuisines: [],
      news: [],
      filters: [],
      selectedFilter: "all",
      isFilterPanelVisible: false,
      modalData: {
        cuisine_name: "",
        ingredients: [],
        cuisine_image: ""
      },
      ingredients: [
        "Olive oil",
        "Garlic",
        "Onion",
        "Vegetable oil",
        "Pepper",
        "Chicken",
        "Tomato",
        "Potato",
        "Carrot",
        "flour",
        "Tomato puree",
        "Orange",
        "Bread",
        "Mushroom",
        "Coriander",
        "Sunflower oil",
        "White wine",
        "Milk",
        "Pork sausage",
        "courgettes",
        "lemon",
        "honey",
        "rice",
        "beans",
        "edible flowers",
        "sesame seeds",
        "mango",
        "cinnamon",
        "mayonnaise",
        "butter",
        "cumin"
      ],
      filterForm: {
        vegan: "false",
        vegetarian: "false",
        spicy: "0",
        cuisine_name: "",
        ingredients: [],
        country_cuisine: "",
        time_to_cook: ""
      }
    };
  },
  async fetch() {
    this.cuisines = await fetch(
      process.env.BACKEND_BASE_URL + "cuisines"
    ).then(res => res.json());
    this.filters = this.getFilters();
    this.filteredCuisines = this.cuisines;

    this.news = await fetch(process.env.BACKEND_BASE_URL + "news").then(res =>
      res.json()
    );
  },
  methods: {
    resetSearch: async function() {
      this.filterForm = {
        vegan: "false",
        vegetarian: "false",
        spicy: "0",
        cuisine_name: "",
        ingredients: [],
        country_cuisine: "",
        time_to_cook: ""
      };
      this.cuisines = await fetch(
        process.env.BACKEND_BASE_URL + "cuisines"
      ).then(res => res.json());
      this.filters = this.getFilters();
      this.filteredCuisines = this.cuisines;

      this.news = await fetch(process.env.BACKEND_BASE_URL + "news").then(res =>
        res.json()
      );
    },
    addTag(newTag) {
      this.ingredients.push(newTag);
      this.filterForm.ingredients.push(newTag);
    },
    showFilterPanel: function() {
      this.isFilterPanelVisible = !this.isFilterPanelVisible;
    },
    changeFilter: function(name) {
      this.selectedFilter = name;
      if (name == "all") {
        this.filteredCuisines = this.cuisines;
      } else {
        this.filteredCuisines = this.cuisines.filter(
          cuisine => cuisine.cuisine_type === name
        );
      }
    },
    showModal: function(data) {
      this.modalData = data;
      this.$bvModal.show("cuisine-modal");
    },
    getFilters: function() {
      let filters = [];
      this.cuisines.map(cuisine => {
        let index = filters.findIndex(
          element => element.name === cuisine.cuisine_type
        );
        index === -1
          ? filters.push({
              name: cuisine.cuisine_type,
              length: 1
            })
          : (filters[index].length = filters[index].length + 1);
      });
      return filters;
    },
    searchCuisines: function(event) {
      event.preventDefault();

      if (
        this.filterForm.country_cuisine === "" &&
        this.filterForm.time_to_cook === ""
      ) {
        fetch(process.env.BACKEND_BASE_URL + "cuisines/search", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            spicy: this.filterForm.spicy,
            vegetarian: this.filterForm.vegetarian,
            vegan: this.filterForm.vegan,
            cuisine_name: this.filterForm.cuisine_name,
            ingredients: this.filterForm.ingredients
          })
        })
          .then(response => {
            if (response.ok) {
              return response.json();
            } else {
              throw new Error("Something went wrong");
            }
          })
          .then(responseJson => {
            this.cuisines = responseJson;
            this.filters = this.getFilters();
            this.filteredCuisines = this.cuisines;
            this.$toast.success("Search Successfull", {
              duration: 5000
            });
            responseJson.length === 0
              ? this.$toast.success("No cuisines found", {
                  duration: 5000
                })
              : null;
          })
          .catch(error => {
            this.$toast.error(error, {
              duration: 5000
            });
          });
      } else {
        if (
          this.filterForm.country_cuisine !== "" &&
          this.filterForm.time_to_cook !== ""
        ) {
          this.cuisines = this.cuisines.filter(
            cuisine =>
              cuisine.country_cuisine.indexOf(
                this.filterForm.country_cuisine
              ) !== -1
          );
          this.cuisines = this.cuisines.filter(cuisine =>
            cuisine.time_to_cook.match(
              new RegExp(this.filterForm.time_to_cook, "gi")
            )
          );
          this.filters = this.getFilters();
          this.filteredCuisines = this.cuisines;
          this.$toast.success("Search Successfull", {
            duration: 5000
          });
          this.cuisines.length === 0
            ? this.$toast.success("No cuisines found", {
                duration: 5000
              })
            : null;
        } else if (this.filterForm.time_to_cook !== "" && this.filterForm.country_cuisine === "") {
          this.cuisines = this.cuisines.filter(cuisine =>
            cuisine.time_to_cook.match(
              new RegExp(this.filterForm.time_to_cook, "gi")
            )
          );
          this.filters = this.getFilters();
          this.filteredCuisines = this.cuisines;
          this.$toast.success("Search Successfull", {
            duration: 5000
          });
          this.cuisines.length === 0
            ? this.$toast.success("No cuisines found", {
                duration: 5000
              })
            : null;
        } else if (this.filterForm.country_cuisine !== "" && this.filterForm.time_to_cook === "") {
          this.cuisines = this.cuisines.filter(
            cuisine =>
              cuisine.country_cuisine.indexOf(
                this.filterForm.country_cuisine
              ) !== -1
          );
          this.filters = this.getFilters();
          this.filteredCuisines = this.cuisines;
          this.$toast.success("Search Successfull", {
            duration: 5000
          });
          this.cuisines.length === 0
            ? this.$toast.success("No cuisines found", {
                duration: 5000
              })
            : null;
        }
      }
    }
  },
  fetchOnServer: false
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped>
.bg {
  margin-top: 20px;
  height: 391px;
  border-radius: 20px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-image: url("~/assets/bg.png");
}

.mainHeading {
  color: var(--white-color);
  position: absolute;
  font-style: italic;
  font-weight: 700;
  top: 290px;
  left: 50px;
  width: 400px;
}

.newsStrip {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: var(--white-color);
  padding: 28px 0 16px;
  margin-top: 20px;
  border-radius: 30px;
  background-color: var(--secondary-color);
}

.newsStripStart {
  margin: 0 10px;
}

.marquee {
  width: 100%;
  margin: 0 auto;
  white-space: nowrap;
  overflow: hidden;
  position: absolute;
}

.marquee .marqueeSpan {
  display: inline-block;
  padding-left: 100%;
  animation: marquee 50s linear infinite;
}

.marquee p {
  display: inline-block;
}

@keyframes marquee {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(-100%, 0);
  }
}

.searchBar {
  margin-top: 60px;
  display: flex;
  justify-content: space-between;
}

.ourMealsHeading {
  display: flex;
  align-items: center;
  font-size: 24px;
  font-weight: 700;
  color: var(--primary2-color);
}

.searchInputContainer {
  display: flex;
  padding: 10px 15px;
  border-radius: 60px;
  align-items: center;
  justify-content: space-between;
  background-color: var(--bg-grey);
}

.searchInput {
  width: 300px;
  border: none;
  outline: none;
  margin-right: 10px;
  background-color: var(--bg-grey);
}

.filterContainer {
  width: 410px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.filter {
  cursor: pointer;
  padding: 7px 10px 11px 10px;
  border-radius: 50%;
  transform: rotate(90deg);
  background-color: var(--primary-color);
}

.filter:hover {
  background-color: var(--primary-hover-color);
}

.filterCheckBoxContainer {
  margin: 20px 0 30px;
  display: flex;
  flex-flow: row wrap;
}

.filterCheckBoxWrap {
  margin-top: 20px;
}

.filterCheckBox {
  cursor: pointer;
  padding: 5px 25px;
  margin: 0 15px 0 0;
  border-radius: 50px;
  color: var(--secondary-color);
  background-color: var(--bg-grey);
}

.filterCheckBox:hover {
  color: var(--white-color);
  background-color: var(--primary-color);
}

.filterCheckBoxActive {
  cursor: pointer;
  padding: 5px 25px;
  margin: 0 15px 0 0;
  border-radius: 50px;
  color: var(--white-color);
  background-color: var(--primary-color);
}

.recipeContainer {
  display: flex;
  margin-top: 50px;
  flex-wrap: wrap;
  width: 100%;
}

.cardContainer {
  cursor: pointer;
  width: 32%;
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
  overflow: hidden;
  margin: 0 8px;
}

.cardContent {
  height: 200px;
  padding: 10px 15px;
}

.cardTitleRow {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cardTitleRowModal {
  margin-top: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
}

.cardTitle {
  font-size: 20px;
  letter-spacing: 0.5;
  color: var(--primary2-light-color);
}

.recipeHeart {
  cursor: pointer;
}

.recipeStars {
  margin: 10px 0 20px;
}

.recipeStar {
  margin-right: -5px;
}

.recipeStarOpaque {
  margin-right: -5px;
  opacity: 0.2;
}

.recipeVegan {
  margin-left: 10px;
}

.recipeTagsContainer {
  display: flex;
}

.recipeTagsContainerModal {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.recipeTag {
  font-size: 12px;
  cursor: pointer;
  padding: 5px 10px;
  margin: 0 5px 0 0;
  border-radius: 50px;
  color: var(--secondary-color);
  background-color: var(--bg-grey);
}

.recipeTime {
  font-size: 12px;
}

.recipeTime span {
  background-color: var(--secondary-color);
  border-radius: 50%;
}

.filterPanel {
  display: flex;
  text-align: center;
  flex-wrap: wrap;
  width: 100%;
  margin-top: 20px;
  padding: 30px 20px;
  border-radius: 20px;
  transition: 0.3s height ease-in;
  background-color: var(--bg-grey);
}

.filterPanelRow {
  width: 100%;
}

.filterPanelRow2 {
  width: 100%;
  margin-top: 10px;
}

.filterFormInput {
  margin-right: 10px;
}

.formBtn {
  width: 100px;
  background-color: var(--primary-color);
}

.formBtnSec {
  width: 100px;
  background-color: var(--secondary-color);
}
</style>
