<template>
  <div>
    <div class="bg">
      <div class="loginContainer">
        <h2 class="formHeading">Login</h2>
        <b-form-input placeholder="Email" class="formInput"></b-form-input>
        <b-form-input placeholder="Password" class="formInput"></b-form-input>
        <b-button class="formBtn">Login</b-button>
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
