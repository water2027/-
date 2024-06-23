// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      2024-06-23
// @description  try to take over the world!
// @author       You
// @match        https://lms.sysu.edu.cn/mod/forum/view.php*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=sysu.edu.cn
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {//不是视频而是讨论的时候使用的脚本
    'use strict';
    let myStatus = document.getElementsByClassName('tips-completion')[0]
    let next = document.getElementById('next-activity-link')
    if(!myStatus){
        next.click()
    }


    // Your code here...
})();
