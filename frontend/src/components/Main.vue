<template>
  <main class="main">
    <div class="welcome">
      <form class="nick-form">
        <label for="nick" class="label">
          Wpisz swój nick:
          <input type="text" id="nick" name="nick" placeholder="Nick" class="input" v-model="nick" />
        </label>
        <button class="btn btn--ok" @click="handleClick">OK</button>
      </form>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      nick: ''
    }
  },
  methods: {
    handleClick: function(e) {
      e.preventDefault();

      console.log(this.nick);
    }
  }
}
</script>