<template>

    <!-- Header  -->
    <Header />

    <!-- 开屏  -->
    <section>
      <!-- Container -->
      <div
        class="mx-auto w-full max-w-7xl px-5  md:px-10"
        data-aos="fade-up"
        data-aos-duration="900"
      >
        <!-- Component -->
        <div
          class="grid grid-cols-1 items-center gap-12 sm:gap-20 md:grid-cols-2"
        >
          <!-- Heading Div -->
          <div class="max-w-[720px] lg:max-w-[842px]">
            <h1 class="mb-4 text-4xl font-semibold md:text-6xl">
              使用Python在线
              <span class="before:block before:absolute before:-inset-1 before:-skew-y-3 before:bg-pink-500 relative inline-block">
                <span class="relative text-white">数据分析</span>
              </span>
            </h1>
            <p
              class="mb-6 max-w-[528px] text-xl text-[#636262] md:mb-10 lg:mb-12"
            >
              无需配置复杂环境，即开即用
            </p>
            <router-link to="/upload" class="mb-6 inline-block rounded-xl bg-amber-300 px-8 py-4 text-center font-semibold text-blue [box-shadow:rgb(22,_133,_169)_6px_6px] md:mb-10 lg:mb-12">
              开始使用
            </router-link>
            <!-- Customers Div -->
          </div>
          <!-- Image Div -->
          <div
            class="relative left-4 h-full max-h-[562px] w-[85%] overflow-visible md:left-0 md:w-[95%] lg:w-full"
          >
            <Vue3Lottie :animationData="SendJSON" 
              class="mx-auto block h-full w-full max-w-[800px] rounded-2xl object-cover" />
          </div>
        </div>
      </div>
    </section>

    <!-- 如何工作 -->
    <section>
      <!-- Container -->
      <div
        class="max-w-7xl px-5 py-16 md:px-10 md:py-16 lg:py-24 mx-auto"
        data-aos="fade-up"
        data-aos-duration="900"
      >
        <!-- Heading Div -->
        <div class="mx-auto w-full max-w-3xl">
          <!-- Component -->
          <div class="text-center">
            <h2 class="text-3xl font-semibold md:text-5xl">
              为何如此
              <span class="before:block before:absolute before:-inset-1 before:-skew-y-3 before:bg-lime-500 relative inline-block">
                <span class="relative text-white">简单</span>
              </span>
            </h2>
            <div class="mx-auto mb-8 mt-4 max-w-[528px] md:mb-12 lg:mb-16">
              <p class="text-[#636262]">
                只需三步，为您搞定数据分析
              </p>
            </div>
          </div>
        </div>
        <!-- How it Works Div -->
        <div
          class="mx-auto grid grid-cols-1 gap-4 sm:justify-items-stretch md:grid-cols-3 lg:gap-8"
          data-aos="fade-up"
          data-aos-duration="900"
        >
          <!-- How it Works Item -->
          <div
            class="relative flex flex-col items-center gap-4 p-8 text-center"
          >
            <div
              class="mb-5 flex max-w-[400px] flex-col items-center justify-center rounded-xl border border-solid border-black bg-green-100 px-8 py-5 [box-shadow:rgb(0,_0,_0)_4px_4px] md:mb-6 lg:mb-8"
            >
              <p class="text-xl font-bold">1</p>
            </div>
            <p class="mb-2 text-xl font-semibold">上传文件</p>
            <p class="text-xs text-[#636262]">
              文件需为CSV格式，大小不超过4Mb
            </p>
            <img
              src="https://assets.website-files.com/63904f663019b0d8edf8d57c/639833af1925275b6f0b43e1_Vector%2032.svg"
              alt=""
              class="absolute bottom-[-33%] left-0 right-auto top-auto -z-10 hidden w-96 md:bottom-auto md:left-[136px] md:right-[-50%] md:top-[18%] md:inline-block lg:left-auto"
            />
          </div>
          <!-- How it Works Item -->
          <div
            class="relative flex flex-col items-center gap-4 p-8 text-center"
          >
            <div
              class="mb-5 flex max-w-[400px] flex-col items-center justify-center rounded-xl border border-solid border-black bg-green-300 px-8 py-5 [box-shadow:rgb(0,_0,_0)_4px_4px] md:mb-6 lg:mb-8"
            >
              <p class="text-xl font-bold">2</p>
            </div>
            <p class="mb-2 text-xl font-semibold">分析数据</p>
            <p class="text-xs text-[#636262]">
              Python后端调用Numpy、Pandas等数据分析库进行分析
            </p>
            <img
              src="https://assets.website-files.com/63904f663019b0d8edf8d57c/639834731925279c5e0b4ee5_Vector%2033.svg"
              alt=""
              class="absolute bottom-[-33%] left-0 right-auto top-auto -z-10 hidden w-96 md:bottom-auto md:left-[136px] md:right-[-50%] md:top-[10%] md:inline-block lg:left-auto"
            />
          </div>
          <!-- How it Works Item -->
          <div
            class="relative flex flex-col items-center gap-4 p-8 text-center"
          >
            <div
              class="mb-5 flex max-w-[400px] flex-col items-center justify-center rounded-xl border border-solid border-black bg-green-500 px-8 py-5 [box-shadow:rgb(0,_0,_0)_4px_4px] md:mb-6 lg:mb-8"
            >
              <p class="text-xl font-bold">3</p>
            </div>
            <p class="mb-2 text-xl font-semibold">返回数据</p>
            <p class="text-xs text-[#636262]">
              前端Vue接收数据并显示
            </p>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 常见疑问 -->
    <section>
      <!-- Container -->
      <div
        class="mx-auto w-full max-w-5xl px-5 pb-16 md:px-10 md:pb-16 lg:pb-24"
      >
        <!-- Heading -->
        <div
          class="mb-8 text-center md:mb-12 lg:mb-16"
          data-aos="fade-up"
          data-aos-duration="900"
        >
          <h2 class="text-3xl font-semibold md:text-5xl">
            常见
            <span class="before:block before:absolute before:-inset-1 before:-skew-y-3 before:bg-teal-500 relative inline-block">
                <span class="relative text-white">疑问</span>
            </span>
          </h2>
        </div>
        <!-- FAQ Container -->
        <div
          class="mb-8 md:mb-12 lg:mb-16"
          data-aos="fade-up"
          data-aos-duration="900"
        >
          <!-- FAQ Item -->
          <div
            class="mb-6 rounded-xl border border-solid border-black p-8"
            x-data="{ open: false }"
          >
            <div
              class="mb-4 flex cursor-pointer items-start justify-between"
              x-on:click.prevent="open = !open"
            >
              <p class="text-xl font-semibold">
                使用了哪些技术?
              </p>
              <div
                class="relative ml-10 flex h-8 w-8 flex-none items-center justify-center rounded-md"
              >
                <Vue3Lottie :animationData="BlingJSON" />
              </div>
            </div>
            <p
              class="mb-4 text-[#636262]"
              x-show="open"
              x-transition:enter="transition ease-out duration-300"
              x-transition:enter-start="transform translate-y--10 opacity-0"
              x-transition:enter-end="transform translate-y-0 opacity-100"
              x-transition:leave="transition ease-in duration-300"
              x-transition:leave-start="transform translate-y-0 opacity-100"
              x-transition:leave-end="transform translate-y--10 opacity-0"
            >
              前端使用Vue3框架，辅以Vite打包，使用TailwindCss调整样式。
              后端使用Django5，调用Numpy、Pandas等数据分析库。
              数据库使用SQLite3。
              项目使用Docker Compose部署。
            </p>
          </div>
          <!-- FAQ Item -->
          <div
            class="mb-6 rounded-xl border border-solid border-black p-8"
            x-data="{ open: false }"
          >
            <div
              class="mb-4 flex cursor-pointer items-start justify-between"
              x-on:click.prevent="open = !open"
            >
              <p class="text-xl font-semibold">
                支持哪些数据分析功能?
              </p>
              <div
                class="relative ml-10 flex h-8 w-8 flex-none items-center justify-center rounded-md "
              >
                <Vue3Lottie :animationData="BlingJSON" />
              </div>
            </div>
            <p
              class="mb-4 text-[#636262]"
              x-show="open"
              x-transition:enter="transition ease-out duration-300"
              x-transition:enter-start="transform translate-y--10 opacity-0"
              x-transition:enter-end="transform translate-y-0 opacity-100"
              x-transition:leave="transition ease-in duration-300"
              x-transition:leave-start="transform translate-y-0 opacity-100"
              x-transition:leave-end="transform translate-y--10 opacity-0"
            >
              支持描述统计的平均数、中位数、众数、标准差、方差、全距、相关系数等。
              推断统计的T检验、方差分析等
            </p>
          </div>
          <!-- FAQ Item -->
          <div
            class="mb-6 rounded-xl border border-solid border-black p-8"
            x-data="{ open: false }"
          >
            <div
              class="mb-4 flex cursor-pointer items-start justify-between"
              x-on:click.prevent="open = !open"
            >
              <p class="text-xl font-semibold">
                其他?
              </p>
              <div
                class="relative ml-10 flex h-8 w-8 flex-none items-center justify-center rounded-md]"
              >
                <Vue3Lottie :animationData="BlingJSON" />
              </div>
            </div>
            <p
              class="mb-4 text-[#636262]"
              x-show="open"
              x-transition:enter="transition ease-out duration-300"
              x-transition:enter-start="transform translate-y--10 opacity-0"
              x-transition:enter-end="transform translate-y-0 opacity-100"
              x-transition:leave="transition ease-in duration-300"
              x-transition:leave-start="transform translate-y-0 opacity-100"
              x-transition:leave-end="transform translate-y--10 opacity-0"
            >
              先凑三个问答框吧，两个不太好看......
            </p>
          </div>
        </div>
        <p class="text-center">
          如果不能解答您的疑惑,
          <a href="https://gitee.com/shaeray/pystats/issues" target="_blank" class="font-bold text-[#457B9D]">点击此处与我联系</a
          >
        </p>
      </div>
    </section>

    <!-- Footer  -->
    <Footer />

</template>

<script setup>
import { Vue3Lottie } from 'vue3-lottie'
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'

import SendJSON from '../assets/animations/send.json'
import BlingJSON from '../assets/animations/bling.json'
</script>

<style>
    a:hover {
	    color: #21a675; /*鼠标移动到链接的颜色*/
    }
 
    a:active {
	    color: #7fecad; /*鼠标点击时的颜色*/
    }
 
    a {
    	text-decoration: none; /*去掉下划线*/
    }

</style>
