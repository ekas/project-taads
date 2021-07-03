<template>
  <div>
    <div class="bg">
      <div class="registerContainer">
        <h2 class="formHeading">Register</h2>
        <b-form @submit="onSubmit">
          <b-form-input
            type="text"
            placeholder="Full Name"
            v-model="form.name"
            class="formInput"
            trim
            required
          ></b-form-input>
          <b-form-input
            type="email"
            placeholder="Email"
            v-model="form.email"
            class="formInput"
            required
          ></b-form-input>
          <b-form-input
            type="password"
            placeholder="Password"
            v-model="form.password"
            class="formInput"
            required
          ></b-form-input>
          <b-form-input
            type="password"
            placeholder="Confirm Password"
            class="formInput"
            required
          ></b-form-input>
          <b-button class="formBtn" type="submit">Register</b-button>
        </b-form>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
export default {
  layout: "header",
  computed: {},
  data() {
    return {
      form: {
        name: "",
        email: "",
        password: ""
      },
      formResponse: ""
    };
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();

      fetch(process.env.BACKEND_BASE_URL + "register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name: this.form.name,
          email: this.form.email,
          password: this.form.password
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
          this.$toast.success("Successfully Registered", {
            duration: 5000
          });
          this.$router.push("/login");
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
  height: calc(100vh - 83px - 50px);
  border-radius: 20px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-image: url("~/assets/bg.png");
  display: flex;
  justify-content: center;
  align-items: center;
}

.registerContainer {
  text-align: center;
  padding: 20px;
  border-radius: 20px;
  background-color: var(--white-color);
  min-height: 100px;
  width: 350px;
}

.formHeading {
  margin-bottom: 30px;
}

.formInput {
  margin: 20px 0 0;
}

.formBtn {
  margin-top: 20px;
  width: 100%;
  background-color: var(--primary-color);
}
</style>
