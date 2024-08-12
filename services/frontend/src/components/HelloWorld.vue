<template>
   <div>
    <p>{{ msg }}</p>
  </div>

  <div>
    <p>{{ serega }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PingComponent',
  data() {
    return {
      msg: '',
      serega:'',
    };
  },
  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    getSerega() {
      axios.get('/serega')
      .then((res) => {
        this.serega = res.data;
      })
      .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
    this.getSerega();
  },
};
</script>
  

