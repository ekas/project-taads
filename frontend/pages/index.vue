<template>
  <div>
    <div fluid class="main">
      <img src="~/assets/logo.png" class="logo" />
      <div class="bg"></div>
      <h1 class="mainHeading">Find Your Favourite Cuisines</h1>
      <p class="newsStrip">
        <img
          src="~/assets/star.svg"
          class="newsStripStart"
          width="15"
          height="15"
        />
        <span>New Recipe Added</span>
        <img
          src="~/assets/star.svg"
          class="newsStripStart"
          width="15"
          height="15"
        />
        <span>New Recipe Added</span>
        <img
          src="~/assets/star.svg"
          class="newsStripStart"
          width="15"
          height="15"
        />
        <span>New Recipe Added</span>
        <img
          src="~/assets/star.svg"
          class="newsStripStart"
          width="15"
          height="15"
        />
        <span>New Recipe Added</span>
        <img
          src="~/assets/star.svg"
          class="newsStripStart"
          width="15"
          height="15"
        />
        <span>New Recipe Added</span>
        <img
          src="~/assets/star.svg"
          class="newsStripStart"
          width="15"
          height="15"
        />
      </p>
      <div class="searchBar">
        <h3 class="ourMealsHeading">Our Meals</h3>
        <div class="searchInputContainer">
          <div class="searchInputContainer">
            <input
              type="text"
              class="searchInput"
              placeholder="Search by name"
            />
            <img
              src="~/assets/search.svg"
              class="searchIcon"
              width="20px"
              height="20px"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
export default {
  layout: "header"
};
</script>

<style scoped>
.main {
  margin: 15px 50px;
  position: relative;
}

.bg {
  height: 391px;
  border-radius: 20px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-image: url("~/assets/bg.png");
}

.logo {
  top: -69px;
  left: -20px;
  position: absolute;
  width: 180px;
}

.mainHeading {
  color: var(--white-color);
  position: absolute;
  font-style: italic;
  font-weight: 700;
  top: 250px;
  left: 30px;
  width: 400px;
}

.newsStrip {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: var(--white-color);
  padding: 10px 20px;
  margin-top: 20px;
  border-radius: 30px;
  background-color: var(--secondary-color);
}

.newsStripStart {
  margin: 0 10px;
}

.searchBar {
  margin-top: 60px;
  display: flex;
  justify-content: space-between;
}

.ourMealsHeading {
  font-size: 18px;
  font-weight: 700;
  color: var(--primary-color);
}

.searchInputContainer {
  display: flex;
  padding: 5px 8px;
  border-radius: 60px;
  align-items: center;
  justify-content: space-between;
  background-color: var(--bg-grey);
}

.searchInput {
  width: 300px;
  border: none;
  outline: none;
  background-color: var(--bg-grey);
}
</style>
