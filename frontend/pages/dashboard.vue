<template>
  <div>
    <div class="bg">
      <div class="loginContainer">
        <h2 class="formHeading">My Dashboard</h2>
        <b-form class="form" v-if="isLoggedIn" @submit="onSubmit">
          <b-row>
            <b-col>
              <b-form-group
                label="Country of Origin"
                description="Please mention which country you belong to."
              >
                <b-form-input
                  type="text"
                  v-model="form.country_origin"
                  placeholder="Germany"
                  trim
                  required
                >
                </b-form-input>
              </b-form-group>
              <b-form-group
                label="Cuisine Name"
                description="Please mention name of your favorite cuisine."
              >
                <b-form-input
                  type="text"
                  v-model="form.cuisine_name"
                  placeholder="Chicken Platter"
                  trim
                  required
                >
                </b-form-input>
              </b-form-group>
              <b-form-group
                label="Ingredients of your cuisine"
                description="Please mention the quantity as well as given in example."
              >
                <b-form-tags
                  no-outer-focus
                  class="mb-2"
                  v-model="form.ingredients"
                >
                  <template
                    v-slot="{
                      tags,
                      inputAttrs,
                      inputHandlers,
                      addTag,
                      removeTag
                    }"
                  >
                    <b-input-group aria-controls="my-custom-tags-list">
                      <input
                        v-bind="inputAttrs"
                        v-on="inputHandlers"
                        placeholder="Ex. 2x400g cans chopped tomatoes"
                        class="form-control"
                      />
                      <b-input-group-append>
                        <b-button @click="addTag()" variant="primary"
                          >Add</b-button
                        >
                      </b-input-group-append>
                    </b-input-group>
                    <ul
                      id="my-custom-tags-list"
                      class="list-unstyled d-inline-flex flex-wrap mb-0"
                      aria-live="polite"
                      aria-atomic="false"
                      aria-relevant="additions removals"
                    >
                      <b-card
                        v-for="tag in tags"
                        :key="tag"
                        :id="`my-custom-tags-tag_${tag.replace(/\s/g, '_')}_`"
                        tag="li"
                        class="mt-1 mr-1"
                        body-class="py-1 pr-2 text-nowrap"
                      >
                        <strong>{{ tag }}</strong>
                        <b-button
                          @click="removeTag(tag)"
                          variant="link"
                          size="sm"
                          :aria-controls="
                            `my-custom-tags-tag_${tag.replace(/\s/g, '_')}_`
                          "
                          >remove</b-button
                        >
                      </b-card>
                    </ul>
                  </template>
                </b-form-tags>
              </b-form-group>
              <b-form-group
                label="Origin of Cuisine"
                description="Please provide countries cuisine is originated from or famous in."
              >
                <b-form-tags v-model="form.country_cuisine"></b-form-tags>
              </b-form-group>
              <b-form-group
                label="Time to cook"
                description="Please provide time range in minutes."
              >
                <b-form-input
                  type="text"
                  v-model="form.time_to_cook"
                  placeholder="20-30"
                  required
                  trim
                >
                </b-form-input>
              </b-form-group>
              <b-form-checkbox
                id="checkbox-1"
                v-model="form.vegetarian"
                name="checkbox-1"
                value="true"
                unchecked-value="false"
              >
                Vegetarian
              </b-form-checkbox>
              <b-form-checkbox
                id="checkbox-2"
                v-model="form.vegan"
                name="checkbox-1"
                value="true"
                unchecked-value="false"
              >
                Vegan
              </b-form-checkbox>
              <b-form-group label="Spice Level" v-slot="{ ariaDescribedby }">
                <b-form-radio
                  v-model="form.spicy"
                  :aria-describedby="ariaDescribedby"
                  name="some-radios"
                  value="1"
                >
                  1
                </b-form-radio>
                <b-form-radio
                  v-model="form.spicy"
                  :aria-describedby="ariaDescribedby"
                  name="some-radios"
                  value="2"
                >
                  2
                </b-form-radio>
                <b-form-radio
                  v-model="form.spicy"
                  :aria-describedby="ariaDescribedby"
                  name="some-radios"
                  value="3"
                >
                  3
                </b-form-radio>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group
                label="Avatar"
                label-for="input-1"
                class="formAvatar"
              >
                <b-avatar text="Add Avatar" class="avatar"></b-avatar>
              </b-form-group>
            </b-col>
          </b-row>
          <div class="btnContainer">
            <b-button class="formBtn" type="submit">Submit</b-button>
            <b-button class="formBtn">Logout</b-button>
          </div>
        </b-form>
        <p v-else>Please login to see your dashboard</p>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
export default {
  layout: "header",
  data() {
    return {
      form: {
        country_origin: "",
        cuisine_name: "",
        ingredients: [],
        time_to_cook: "20",
        country_cuisine: ["Germany", "France"],
        spicy: "1",
        vegetarian: "false",
        vegan: "false"
      },
      isLoggedIn: process.server ? "" : !!localStorage.getItem("authToken")
    };
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();

      fetch(process.env.BACKEND_BASE_URL + "users", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("authToken")}`
        },

        body: JSON.stringify({
          avatar: "https://placekitten.com/300/300",
          country_origin: this.form.country_origin,
          cuisine_name: this.form.cuisine_name,
          ingredients: this.form.ingredients,
          country_cuisine: this.form.country_cuisine,
          time_to_cook: this.form.time_to_cook,
          spicy: this.form.spicy,
          vegetarian: this.form.vegetarian,
          vegan: this.form.vegan
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
          this.formResponse = responseJson;
          this.$toast.success("Recipe Added", {
            duration: 5000
          });
        })
        .catch(error => {
          this.$toast.error(error, {
            duration: 5000
          });
        });
    }
  },
  fetchOnServer: false
};
</script>

<style scoped>
.bg {
  margin-top: 20px;
  border-radius: 20px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-image: url("~/assets/bg.png");
  display: flex;
  justify-content: center;
  align-items: center;
}

.loginContainer {
  text-align: center;
  padding: 20px;
  border-radius: 20px;
  background-color: var(--white-color);
  width: 100%;
  /* height: 100%; */
  margin: 220px;
}

.form {
  text-align: left;
}

.formHeading {
  margin-bottom: 30px;
}

.formInput {
  margin: 20px 0;
}

.btnContainer {
  text-align: center;
}

.formBtn {
  width: 200px;
  background-color: var(--primary-color);
}

.formAvatar {
  text-align: center;
}

.avatar {
  width: 150px;
  height: 150px;
}
</style>
