<template>

    <!-- Header  -->
    <Header />

    <!-- 数据  -->
    <section>
        <div class="overflow-x-auto pb-10">
            <table class="table table-xs">
                <thead>
                <tr>
                    <th v-for="(header, index) in headers" :key="index">{{ header }}</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(row, index) in data" :key="index" class="hover">
                    <td v-for="(value, key) in row" :key="key">{{ value }}</td>
                </tr>
                </tbody>
                <tfoot>
                <tr>
                    <th v-for="(header, index) in headers" :key="index">{{ header }}</th>
                </tr>
                </tfoot>
            </table>
        </div>
    </section>
    
    <!-- 跳转  -->
    <router-link to="/analysis" class="mb-6 inline-block rounded-xl hover:text-white bg-cyan-500 px-8 py-4 text-center font-semibold text-blue [box-shadow:rgb(22,_133,_169)_6px_6px] md:mb-10 lg:mb-12">
              开始处理
    </router-link>

    <Footer />

</template>

<script setup>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import { computed } from 'vue';
import { useStore } from 'vuex';

const store = useStore();

// 使用 computed 从 store 中获取数据
const data = computed(() => store.state.tableData);

// 获取表头
const headers = computed(() => {
    if (data.value.length > 0) {
        return Object.keys(data.value[0]);
    }
    return [];
});
</script>

<style>
</style>
