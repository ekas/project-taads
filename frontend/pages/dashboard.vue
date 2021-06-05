<template>
  <div>
    <div class="bg">
      <div class="loginContainer">
        <h2 class="formHeading">My Dashboard</h2>
        <b-form class="form">
          <b-row>
            <b-col>
              <b-form-group
                label="Country of Origin"
                label-for="input-1"
                description="Please mention which country you belong to.."
              >
                <b-form-input
                  id="input-1"
                  type="email"
                  placeholder="Germany"
                  required
                >
                </b-form-input>
              </b-form-group>
              <b-form-group
                label="Ingredients of your cuisine"
                label-for="input-1"
                description="Please mention the quantity as well as given in example."
              >
                <b-form-tags no-outer-focus class="mb-2">
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
                label-for="input-2"
                description="Please provide countries cuisine is originated from or famous in."
              >
                <b-form-tags
                  input-id="tags-basic"
                  v-model="value"
                ></b-form-tags>
              </b-form-group>
              <b-form-group
                label="Time to cook"
                label-for="input-2"
                description="Please provide time range in minutes."
              >
                <b-form-input
                  id="input-2"
                  type="string"
                  placeholder="20-30"
                  required
                >
                </b-form-input>
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
            <b-button class="formBtn">Submit</b-button>
          </div>
        </b-form>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
export default {
  layout: "header",
  data() {
    return {
      value: ["Germnay", "France"]
    };
  }
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
  margin: 100px;
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
