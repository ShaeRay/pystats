<template>
    <div class="navbar bg-base-100">
        <div class="navbar-start">
            <a class="btn btn-ghost text-xl">PyStats</a>
        </div>
        <div class="navbar-center hidden md:flex lg:flex">
            <ul class="menu menu-horizontal px-1">
                <li>
                    <router-link to="/">首页</router-link>
                </li>
                <li>
                    <router-link to="/upload">快速开始</router-link>
                </li>
                <li>
                    <router-link to="/api">API文档</router-link>
                </li>
                <li>
                    <router-link to="/api">官方教程</router-link>
                </li>
            </ul>
        </div>
        <div class="navbar-end">
            <a href="http://shaeray.cloud" class="flex items-center">
                <img src="../assets/logo.svg" class="mr-3 h-6 sm:h-9" alt="" />
            </a>
        </div>
    </div>
</template>
