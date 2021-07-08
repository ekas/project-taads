<template>
  <div>
    <div class="bg"></div>
    <h1 class="mainHeading">Find Your Favourite Cuisines</h1>
    <div class="newsStrip">
      <p class="marquee">
        <span class="marqueeSpan" v-for="ticker of news" :key="ticker._id">
          <span>
            <img
              src="~/assets/star.svg"
              class="newsStripStart"
              width="15"
              height="15"
            />
            <p>{{ ticker.title }}</p>
          </span>
          <img
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
        <div class="searchInputContainer">
          <input type="text" class="searchInput" placeholder="Search by name" />
          <img
            src="~/assets/search.svg"
            class="searchIcon"
            width="20px"
            height="20px"
          />
        </div>
        <div class="filter">
          <img
            src="~/assets/settings.svg"
            class="searchIcon"
            width="20px"
            height="20px"
          />
        </div>
      </div>
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
              v-if="cuisine.spicy === true"
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
  </div>
</template>
<script lang="ts">
export default {
  layout: "header",
  data() {
    return {
      cuisines: [],
      filteredCuisines: [],
      news: [],
      filters: [],
      selectedFilter: "all"
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
    getFilters: function() {
      let filters = [];
      this.cuisines.map(cuisine => {
        debugger;
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
    }
  },
  fetchOnServer: false
};
</script>

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
  justify-content: space-between;
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
  justify-content: space-between;
  width: 100%;
}

.cardContainer {
  width: 32%;
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
  overflow: hidden;
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
</style>
