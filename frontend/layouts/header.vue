<template>
  <div class="main">
    <nav>
      <b-container fluid class="header">
        <NuxtLink
          to="/"
          class="headerItem"
          :class="$route.name === 'index' ? 'active' : ''"
        >
          Search
        </NuxtLink>
        <NuxtLink
          to="/login"
          class="headerItem"
          :class="$route.name === 'login' ? 'active' : ''"
        >
          Login
        </NuxtLink>
        <NuxtLink
          to="/register"
          class="headerItem"
          :class="$route.name === 'register' ? 'active' : ''"
        >
          Register
        </NuxtLink>
        <NuxtLink
          to="/dashboard"
          class="headerItem"
          :class="$route.name === 'dashboard' ? 'active' : ''"
        >
          My Dashboard
        </NuxtLink>
      </b-container>
    </nav>
    <img src="~/assets/logo.png" class="logo" />

    <Nuxt />
  </div>
</template>
<style scoped>
.main {
  margin: 15px 50px 50px;
  position: relative;
}

.logo {
  top: -2px;
  left: -20px;
  position: absolute;
  width: 180px;
}

.header {
  padding-top: 20px;
  display: flex;
  justify-content: flex-end;
}

.headerItem {
  color: #000;
  padding: 0 5px;
  margin: 0 30px;
  text-decoration: none;
}

.active {
  border-bottom: var(--primary-color) solid 4px;
}

.headerItem:hover {
  color: var(--primary-hover-color);
}
</style>
