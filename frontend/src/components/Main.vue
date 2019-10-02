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
    </div>
  </main>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      nick: "",
      isLogged: localStorage.getItem("name")
    };
  },
  methods: {
    isUserLogged: function(e) {
      if (localStorage.getItem("name")) {
        this.isLogged = true;
        return true;
      } else {
        this.isLogged = false;
        return false;
      }
    },

    userAddedOK: function(e) {
      localStorage.setItem("name", this.nick);
      this.isLogged = true;
      console.log(this.isLogged);
    },

    handleClick: function(e) {
      e.preventDefault();

      if (!this.isUserLogged()) {
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
  }
};
</script>