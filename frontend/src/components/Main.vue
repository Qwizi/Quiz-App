<template>
  <main class="main">
    <div class="welcome">
      <form class="nick-form" v-if="!isLogged">
        <label for="name" class="label">
          Wpisz swój nick:
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Name"
            class="input"
            v-model="name"
          />
        </label>
        <button class="btn btn--ok" @click="handleNickFormClick">OK</button>
      </form>
      <div class="header" v-else>Witaj, {{name}}</div>
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
      name: localStorage.getItem("name") ? localStorage.getItem("name") : "",
      isLogged: !!localStorage.getItem("name"),
    };
  },
  methods: {
    setName: function(value) {
      localStorage.setItem("name", value);
      this.isLogged = true;
    },
    handleNickFormClick: function(e) {
      e.preventDefault();

      if (!this.isLogged) {
        axios
          .post(`http://localhost:8000/user/`, { name: this.name })
          .then(res => {
            this.setName(res.data.name);
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