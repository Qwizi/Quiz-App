<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
$bg-color: #757575;
$light: #a4a4a4;
$dark: #494949;
$text: #fff;

$footer-height: 50px;

@mixin flex {
  display: flex;
  justify-content: center;
  align-items: center;
}

html {
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: inherit;
  -webkit-font-smoothing: antialiased;
  -moz-osx-smoothing: grayscale;
}

body {
  margin: 0;
  font-family: "Roboto Mono", monospace;
  background-color: $bg-color;
  color: $text;
}

h1 {
  margin: 0;
  padding: 0;
}

label {
  display: flex;
  align-items: center;
}

.wrapper {
  max-width: 1200px;
  margin: auto;
  min-height: 100%;
  display: flex;
  flex-direction: column;
}

.page-header {
  padding: 10px;
  background-color: $dark;
}

.main {
  padding: 10px;
  background-color: $light;
  flex: 1;
}

.welcome {
  text-align: center;
  width: fit-content;
  margin: auto;
  padding: 10px;
}

.label,
.btn--ok {
  display: inline-block;
}

.input {
  padding: 5px;
}

.btn {
  padding: 5px;
  min-width: 50px;
  background-color: $dark;
  border: none;
  color: $text;
  cursor: pointer;
}

.page-footer {
  min-height: $footer-height;
}

.page-footer {
  @include flex;
  padding: 10px;
  background-color: $dark;
}
</style>
