<template>
    <footer class="bg-white dark:bg-gray-800 pt-12  ">
        <div class="max-w-screen-lg px-4 mx-auto text-gray-400 xl:max-w-screen-xl sm:px-6 md:px-8 dark:text-gray-300">
            <ul class="flex flex-wrap justify-center pb-4 text-lg font-light">
                <li class="w-1/2 md:w-1/3 lg:w-1/3">
                    <div class="text-center">
                        <h2 class="text-gray-500 dark:text-gray-200 text-md uppercase mb-4">
                            文档
                        </h2>
                        <ul>
                            <li class="mb-4 transition-colors duration-200 hover:text-gray-800 dark:hover:text-white">
                                <router-link to="/api">API文档</router-link>
                            </li>
                            <li class="mb-4 transition-colors duration-200 hover:text-gray-800 dark:hover:text-white">
                                <router-link to="/guide">使用教程</router-link>
                            </li>
                        </ul>
                    </div>
                </li>
                <li class="w-1/2 md:w-1/3 lg:w-1/3">
                    <div class="text-center">
                        <h2 class="text-gray-500 dark:text-gray-200 text-md uppercase mb-4">
                            代码仓库
                        </h2>
                        <ul>
                            <li class="mb-4 transition-colors duration-200 hover:text-gray-800 dark:hover:text-white">
                                <a href="https://github.com/ShaeRay/pystats"  target="_blank">
                                    Github
                                </a>
                            </li>
                            <li class="mb-4 transition-colors duration-200 hover:text-gray-800 dark:hover:text-white">
                                <a href="https://gitee.com/shaeray/pystats"  target="_blank">
                                    Gitee
                                </a>
                            </li>
                        </ul>
                    </div>
                </li>
            </ul>
            <div class="text-center pt-4 sm:pt-6 font-light flex items-center justify-center">
                Created by ShaeRay
            </div>
            <div class="text-center font-light flex items-center justify-center">
                <a href="https://beian.miit.gov.cn/" target="_blank" class=" text-xs pt-1 active:text-cyan-300 hover:text-cyan-500">皖ICP备2024042528号</a>
            </div>
        </div>
    </footer>
</template>