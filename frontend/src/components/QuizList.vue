<template>
    <div class="quiz-list">
        <ul v-for="quiz_data in this.quizzes">
            <li v-for="quiz in quiz_data">
                {{ quiz.title }}
            </li>
        </ul>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                quizzes: []
            }
        },
        created() {
            axios.get('http://localhost:8000/quiz/')
                .then(res => {
                    this.quizzes.push(res.data);
                    console.log(this.quizzes);
                })
                .catch(error => console.log(error));
        }
    }
</script>