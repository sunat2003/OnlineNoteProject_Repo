first=document.querySelector(".first")
menulist=document.querySelector(".menulist")


first.addEventListener("click",
    ()=>{
        menulist.classList.toggle('active1')
        console.log("Sunat")
    }
)