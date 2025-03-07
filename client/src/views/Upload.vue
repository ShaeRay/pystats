<template>

  <!-- Header  -->
  <Header />

  <!-- 文件上传  -->
  <section>
    <!-- Container -->
    <div
      class="mx-auto w-full max-w-7xl px-5  md:px-10 pb-2"
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
            点击按钮
            <span class="before:block before:absolute before:-inset-1 before:-skew-y-3 before:bg-sky-500 relative inline-block">
              <span class="relative text-white">上传文件</span>
            </span>
          </h1>
          <p
            class="mb-6 max-w-[528px] text-xl text-[#636262] md:mb-10 lg:mb-12"
          >
            仅支持4MB以下的CSV文件
          </p>

          <input 
            type="file" 
            accept=".csv" 
            class="file-input file-input-success w-full max-w-xs" 
            @change="handleFileUpload"
          />
        </div>
        <!-- Image Div -->
        <div
          class="relative left-4 h-full max-h-[562px] w-[85%] overflow-visible md:left-0 md:w-[95%] lg:w-full"
        >
          <Vue3Lottie :animationData="CodeJSON" 
            class="mx-auto block h-full w-full max-w-[800px] rounded-2xl object-cover bgw" />
        </div>
      </div>
    </div>
  </section>

  <!-- Footer  -->
  <Footer />
  
</template>

<script setup>
import { Vue3Lottie } from 'vue3-lottie'
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import CodeJSON from '../assets/animations/code.json'

import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import axios from 'axios'

const store = useStore()
const router = useRouter()

//1.处理上传逻辑
const handleFileUpload = (event) => {
  const file = event.target.files[0]
  const isCSV = file.type === 'text/csv'
  const isLt4M = file.size / 1024 / 1024 < 4
  
  //如果不是CSV
  if (!isCSV) {
    alert('上传文件只能是 CSV 格式!')
    return flase
  }

  //如果大于4Mb
  if (!isLt4M) {
    alert('上传文件大小不能超过 4MB!')
    return flase
  }

  //确认无误
  // 创建 FormData 对象
  const formData = new FormData()
  formData.append('file', file)
  
  // 使用 axios 上传文件
  axios.post('http://127.0.0.1:8000/api/upload/', formData)
  .then(response => {
    handleSuccess(response)
  })
  .catch(error => {
    handleError(error)
  })
}

//2.上传成功
const handleSuccess = (response) => {
  if (response && response.data) {
    const data = JSON.parse(response.data)
    if (Array.isArray(data)) {
      store.dispatch('updateTableData', data)
      router.push({ name: 'Table' })
    } else {
      console.error('服务端响应格式不对:', response)
    }
  } else {
    console.error('服务端响应格式不对:', response)
  }
}

//3.上传失败
const handleError = (err) => {
  console.error('Upload failed:', err)
  alert('上传失败!')
}
</script>

<style>
</style>
