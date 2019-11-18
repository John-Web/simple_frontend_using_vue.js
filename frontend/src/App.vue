<template>
<div>
<p>Home page</p>
  <p>test: {{ text1 }}</p>
  <input v-model="input" type="text"/>
  <button @click="run">submit</button>
</div>

</template>
<script>
export default {
  data () {
    return {
      text1: "hello",
      input: "",
    }
  },
  methods: {
    run () {
      let params = new URLSearchParams();
      params.append('input', this.input);
      this.axios.get('/api/run', {params: params})
        .then((response) => {
          this.text1 = response.data.text1;
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  }
}

</script>
