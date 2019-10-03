<template>
  <main class="main">
    <div class="welcome">
      <form class="nick-form" v-if="!isLogged">
        <label for="nick" class="label">
          Wpisz swój nick:
          <input
            type="text"
            id="nick"
            name="nick"
            placeholder="Nick"
            class="input"
            v-model="nick"
          />
        </label>
        <button class="btn btn--ok" @click="handleClick">OK</button>
      </form>
      <div class="header" v-else>Witaj, {{nick}}</div>
      <QuizList />
    </div>
  </main>
</template>

<script>
import axios from "axios";
import QuizList from "./QuizList";

export default {
  data() {
    return {
      nick: localStorage.getItem("name") ? localStorage.getItem("name") : "",
      isLogged: !!localStorage.getItem("name"),
    };
  },
  methods: {
    userAddedOK: function() {
      localStorage.setItem("name", this.nick);
      this.isLogged = true;
    },
    handleClick: function(e) {
      e.preventDefault();

      if (!this.isLogged) {
        axios
          .post(`http://localhost:8000/user/`, { name: this.nick })
          .then(res => {
            console.log(JSON.stringify(res));
            return res;
          })
          .then(res => {
            this.userAddedOK();
          })
          .catch(error => console.log(error));
      }
    }
  },
  components: {
    QuizList
  }
};
</script>