// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      2024-06-23
// @description  try to take over the world!
// @author       You
// @match        https://lms.sysu.edu.cn/mod/fsresource/view.php*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=sysu.edu.cn
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';
    let myStatus = document.getElementsByClassName('tips-completion')[0]
    let next = document.getElementById('next-activity-link')
    let isstarted = false
    setInterval(()=>{
        console.log(myStatus.innerText)
        if(myStatus.innerText != '未完成'){
            next.click()
            isstarted = false
        }
        if(!myStatus){
            next.click()
            isstarted = false
        }
    },20000)
    setInterval(()=>{
        if(!isstarted){
            var video = document.getElementsByTagName("video")[0]
            video.muted = true
            video.play()
        }
    },5000)


    // Your code here...
})();
