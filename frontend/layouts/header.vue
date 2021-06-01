<template>
  <nav>
    <b-container fluid class="header">
      <NuxtLink to="/" class="headerItem active">Search</NuxtLink>
      <NuxtLink to="/" class="headerItem">Login</NuxtLink>
      <NuxtLink to="/" class="headerItem">Register</NuxtLink>
    </b-container>
    <Nuxt />
  </nav>
</template>
<style scoped>
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
