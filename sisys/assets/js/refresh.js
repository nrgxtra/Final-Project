var refreshBtns = document.getElementsByClassName('refresh')

for(i = 0; i < refreshBtns.length; i++){
    refreshBtns[i].addEventListener('click', function () {
        location.reload()
    })
}




