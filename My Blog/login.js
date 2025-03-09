// 获取元素
const tab_nav = document.querySelector('.tab-nav')
const tab_pane = document.querySelectorAll('.tab-pane')
// 当登入方式被点击 切换 显示
tab_nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
        // 取消上一个 active
        tab_nav.querySelector('.active').classList.remove('active')
        //当前元素添加 active
        e.target.classList.add('active')
        //干掉所有
        for (let i = 0; i < tab_pane.length; i++) {
            tab_pane[i].style.display = 'none'
        }
        //让对应的序号显示
        tab_pane[e.target.dataset.id].style.display = 'block'
    }

})

const form = document.querySelector('form')
const agree = document.querySelector('[name=agree]')
const uname = document.querySelector('[name=uname]')
const login = document.querySelector('[name=login]')
const regist = document.querySelector('[name=regist]')
// 提交表单事件 登入跳转
form.addEventListener('submit', function (e) {
    //阻止默认事件
    e.preventDefault()
    if (!agree.checked) {
        return alert('请勾选用户协议')
    }
    //成功再跳转
    location.href = 'https://qsj-python.github.io/Awesome-Love-Code/Web/004/'
})