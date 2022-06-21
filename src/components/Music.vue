<template>
  <div id="app" style="text-align:center;">
    <header class="page-header">
  <nav>
    <a href="#0" aria-label="forecastr logo" class="logo">
      <svg width="140" height="49">
        <use xlink:href="#logo"></use>
      </svg>
    </a>
    <button class="toggle-mob-menu" aria-expanded="false" aria-label="open menu">
      <svg width="20" height="20" aria-hidden="true">
        <use xlink:href="#down"></use>
      </svg>
    </button>

    <ul class="admin-menu">
      <li class="menu-heading">
        <h3>Menu</h3>
      </li>

      <li>
        <router-link @click="pause()" to="/exercise2">
          <svg>
            <use xlink:href="#users"></use>
          </svg>
          <span>GIF</span>
        </router-link>
      </li>

      <li>
        <router-link @click="pause()" to="/exercise">
          <svg>
            <use xlink:href="#trends"></use>
          </svg>
          <span >Home</span>
        </router-link>
      </li>

      <li>
        <router-link @click="pause()" to="/music">
          <svg>
            <use xlink:href="#trends"></use>
          </svg>
          <span>Status</span>
        </router-link>
      </li>

      <li class="menu-heading">
        <router-link to="/exercise">
          <svg>
            <use xlink:href="#trends"></use>
          </svg>
          <span >Back</span>
        </router-link>

      </li>
    </ul>
  </nav>
</header>

<div style="text-align:center;">
        <!-- <img v-bind:src="current.image"> -->
        <form>
        <input type="text" name="id" placeholder="Type here" v-model="id">
        <button class="button button5" @click="check()" method="post">
            Check status
        </button>
        {{input}}
    </form>

</div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: 'app',

      mounted(){
          // this.get_status()


      },
  data () {

    return {

    id:""

      }



  },
  methods: {
     async get_status(){
        const path = 'http://localhost:80/get_status'
        console.warn(this.input)
        axios.get(path,this.input)
        .then((response) =>{
          this.list_videos = response.data
          // this.amount = list_videos.length
          console.log(response.data)
          console.log("hi")

        })

        .catch((err)=>{
          console.log(err);

        });
     },
     check(){
      console.warn(this.id)
     }
  }
}


</script>
<style>

::placeholder {
  color: red;
}
.playlist {
  padding: 0px 30px;
}
.playlist h3 {
  color: #212121;
  font-size: 28px;
  font-weight: 400;
  margin-bottom: 30px;
  text-align: center;
}
.playlist .song {
  display: block;
  width: 100%;
  padding: 15px;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
}
.playlist .song:hover {
  color: #FF5858;
}
.playlist .song.playing {
  color: #FFF;
  background-image: linear-gradient(to right, #CC2E5D, #FF5858);
}
</style>
