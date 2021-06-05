<template>
  <div>
    <div class="bg"></div>
    <h1 class="mainHeading">Find Your Favourite Cuisines</h1>
    <div class="newsStrip">
      <p class="marquee">
        <span class="marqueeSpan">
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
        </span>
      </p>
      <p class="marquee marquee2">
        <span>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
          <img
            src="~/assets/star.svg"
            class="newsStripStart"
            width="15"
            height="15"
          />
          <p>New Recipe Added</p>
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
      <span class="filterCheckBoxActive">
        <span>All</span>
        <span> (170)</span>
      </span>
      <span class="filterCheckBox">
        <span>Break Fast</span>
        <span> (23)</span>
      </span>
      <span class="filterCheckBox">
        <span>Lunch</span>
        <span> (41)</span>
      </span>
      <span class="filterCheckBox">
        <span>Drinks</span>
        <span> (53)</span>
      </span>
      <span class="filterCheckBox">
        <span>Desserts</span>
        <span> (33)</span>
      </span>
      <span class="filterCheckBox">
        <span>Fastfood</span>
        <span> (20)</span>
      </span>
    </div>
    <div class="recipeContainer">
      <div class="cardContainer">
        <img src="~/assets/Image1.png" width="100%" height="200px" />
        <div class="cardContent">
          <div class="cardTitleRow">
            <span class="cardTitle">Indian Chicken Platter</span>
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
          </div>
          <div class="cardTitleRow">
            <div class="recipeTagsContainer">
              <span class="recipeTag">
                <span>Indian</span>
              </span>
              <span class="recipeTag">
                <span>Pakistani</span>
              </span>
            </div>
            <div class="recipeTime"><span>we</span> 20-30</div>
          </div>
        </div>
      </div>
      <div class="cardContainer">
        <img src="~/assets/Image2.png" width="100%" height="200px" />
        <div class="cardContent">
          <div class="cardTitleRow">
            <span class="cardTitle">Risotto</span>
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
          </div>
          <div class="cardTitleRow">
            <div class="recipeTagsContainer">
              <span class="recipeTag">
                <span>Italian</span>
              </span>
              <span class="recipeTag">
                <span>European</span>
              </span>
            </div>
            <div class="recipeTime"><span>we</span> 10-20</div>
          </div>
        </div>
      </div>
      <div class="cardContainer">
        <img src="~/assets/Image3.png" width="100%" height="200px" />
        <div class="cardContent">
          <div class="cardTitleRow">
            <span class="cardTitle">Maslenitca</span>
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
          </div>
          <div class="cardTitleRow">
            <div class="recipeTagsContainer">
              <span class="recipeTag">
                <span>Russian</span>
              </span>
            </div>
            <div class="recipeTime"><span>we</span> 25-35</div>
          </div>
        </div>
      </div>
      <div class="cardContainer">
        <img src="~/assets/Image4.png" width="100%" height="200px" />
        <div class="cardContent">
          <div class="cardTitleRow">
            <span class="cardTitle">Moussaka</span>
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
          </div>
          <div class="cardTitleRow">
            <div class="recipeTagsContainer">
              <span class="recipeTag">
                <span>Italian</span>
              </span>
              <span class="recipeTag">
                <span>Greek</span>
              </span>
            </div>
            <div class="recipeTime"><span>we</span> 15-25</div>
          </div>
        </div>
      </div>
      <div class="cardContainer">
        <img src="~/assets/Image5.png" width="100%" height="200px" />
        <div class="cardContent">
          <div class="cardTitleRow">
            <span class="cardTitle">Capachino</span>
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
              class="recipeStarOpaque"
              width="15"
              height="15"
            />
            <img
              src="~/assets/star.svg"
              class="recipeStarOpaque"
              width="15"
              height="15"
            />
          </div>
          <div class="cardTitleRow">
            <div class="recipeTagsContainer">
              <span class="recipeTag">
                <span>American</span>
              </span>
              <span class="recipeTag">
                <span>European</span>
              </span>
            </div>
            <div class="recipeTime"><span>we</span> 20-30</div>
          </div>
        </div>
      </div>
      <div class="cardContainer">
        <img src="~/assets/Image6.png" width="100%" height="200px" />
        <div class="cardContent">
          <div class="cardTitleRow">
            <span class="cardTitle">Arabic Mandi</span>
            <img src="~/assets/heart.svg" width="18px" class="recipeHeart" />
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
          </div>
          <div class="cardTitleRow">
            <div class="recipeTagsContainer">
              <span class="recipeTag">
                <span>Arabic</span>
              </span>
              <span class="recipeTag">
                <span>Turkish</span>
              </span>
            </div>
            <div class="recipeTime"><span>we</span> 35-45</div>
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

.marquee span {
  display: inline-block;
  padding-left: 100%;
  animation: marquee 50s linear infinite;
}

.marquee p {
  display: inline-block;
}

.marquee2 span {
  animation-delay: 0s;
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
  margin-top: 60px;
  display: flex;
}

.filterCheckBox {
  cursor: pointer;
  padding: 5px 25px;
  margin: 0 15px 0 0;
  border-radius: 50px;
  color: var(--secondary-color);
  background-color: var(--bg-grey);
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
  margin-bottom: 20px;
}

.recipeStar {
  margin-right: -5px;
}

.recipeStarOpaque {
  margin-right: -5px;
  opacity: 0.2;
}

.recipeTagsContainer {
  display: flex;
}

.recipeTag {
  font-size: 12px;
  cursor: pointer;
  padding: 5px 25px;
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
