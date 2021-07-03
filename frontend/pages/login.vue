<template>
  <div>
    <div class="bg">
      <div class="loginContainer">
        <h2 class="formHeading">Login</h2>
        <b-form @submit="onSubmit">
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
          <b-button class="formBtn" type="submit">Login</b-button>
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
      form: {
        email: "",
        password: ""
      },
      formResponse: ""
    };
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();

      fetch(process.env.BACKEND_BASE_URL + "login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
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
          if (process.browser) {
            localStorage.setItem("authToken", this.formResponse.token);
          }
          this.$toast.success("Successfully Logged In", {
            duration: 5000
          });
          this.$router.push("/dashboard");
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

.loginContainer {
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
  margin: 20px 0;
}

.formBtn {
  margin-top: 20px;
  width: 100%;
  background-color: var(--primary-color);
}
</style>
