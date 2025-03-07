<template>
    <Header />

    <!-- 开屏  -->
    <section>
      <!-- Container -->
      <div
        class="mx-auto w-full pb-10 max-w-7xl px-5  md:px-10"
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
              触手可得
              <span class="before:block before:absolute before:-inset-1 before:-skew-y-3 before:bg-indigo-500 relative inline-block">
                <span class="relative text-white">统计数据</span>
              </span>
            </h1>
            <p
              class="mb-6 max-w-[528px] text-xl text-[#636262] md:mb-10 lg:mb-12"
            >
              无需配置复杂环境，即开即用
            </p>
            <select v-model="selectedOption" @click="scrollToSection" class="select select-info select-bordered select-lg w-full max-w-xs">
                <option disabled selected value="">选择您需要的统计数据</option>
                <option value="BasicStats">描述统计</option>
                <option value="CorrelationStats">相关系数</option>
                <option value="TTest">T检验</option>
                <option value="Anova">单因素方差分析</option>
            </select>

          </div>

          <!-- 数据分析动画 Div -->
          <div
            class="relative left-4 h-full max-h-[562px] w-[85%] overflow-visible md:left-0 md:w-[95%] lg:w-full"
          >
            <Vue3Lottie :animationData="TableJSON" 
              class="mx-auto block h-full w-full max-w-[800px] rounded-2xl object-cover" />
          </div>
        </div>
      </div>
    </section>

    <!-- 具体数据分析组件  -->
    <section id="section">
        <component v-if="activeComponent" :is="activeComponent"></component>
    </section>

    <Footer />
</template>

<script setup>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import TableJSON from '../assets/animations/table.json'
import { ref, computed } from 'vue'
import BasicStats from '../analysis/BasicStats.vue'
import CorrelationStats from '../analysis/CorrelationStats.vue'
import TTest from '../analysis/TTest.vue'
import Anova from '../analysis/Anova.vue'

const selectedOption = ref('');

const activeComponent = computed(() => {
    const section = document.querySelector('#section');
    switch (selectedOption.value) {
        case 'BasicStats':
            section.scrollIntoView({ behavior: 'smooth' });
            return BasicStats;
        case 'CorrelationStats':
            section.scrollIntoView({ behavior: 'smooth' });
            return CorrelationStats;
        case 'TTest':
            section.scrollIntoView({ behavior: 'smooth' });
            return TTest;
        case 'Anova':
            section.scrollIntoView({ behavior: 'smooth' });
            return Anova;
        default:
            return null;
    }
});
</script>