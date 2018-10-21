function addSeats() {
    var orderedList = document.getElementById("overall")
    //console.log(orderedList)
    var rows = 25
    for(var i = 1; i < rows+1; i++) {
        var item = document.createElement('li');
        item.class = "row row--" + String(i)
        //console.log(item)
        var sub_item = document.createElement('ol')
        sub_item.classList.add("seats")
        sub_item.type = "A"

        for(var j = 0; j < 6; j++) {
            var sub_sub_item = document.createElement('li')
            sub_sub_item.classList.add("seat")
            var sub_sub_sub_item1 = document.createElement('input')
            sub_sub_sub_item1.type = "checkbox"
            var sub_sub_sub_item2 = document.createElement('label')
            var sub_sub_sub_item3 = document.createElement('span')
            sub_sub_sub_item3.innerText = 'Hello'
            sub_sub_sub_item3.classList.add("tooltiptext")
            var special_stuff = ''
            if(j == 0) {
                special_stuff = String(i) + 'A'
            } else if(j == 1) {
                special_stuff = String(i) + 'B'
            } else if(j == 2) {
                special_stuff = String(i) + 'C'
            } else if(j == 3) {
                special_stuff = String(i) + 'D'
            } else if(j == 4) {
                special_stuff = String(i) + 'E'
            } else{
                special_stuff = String(i) + 'F'
            }
            sub_sub_sub_item1.id = special_stuff
            sub_sub_sub_item2.for = special_stuff
            sub_sub_sub_item2.innerText = special_stuff
            sub_sub_sub_item2.id = 'r' + String(j) + 'c' + String(i-1)
            sub_sub_item.appendChild(sub_sub_sub_item1)
            sub_sub_item.appendChild(sub_sub_sub_item2)
            sub_sub_item.appendChild(sub_sub_sub_item3)
            sub_item.appendChild(sub_sub_item)
        }
        item.appendChild(sub_item)
        orderedList.appendChild(item)
    }
}
