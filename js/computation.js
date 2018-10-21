function serverLoader() {
    var url = 'https://seatssavy.appspot.com/getOrder'

    console.log('Sending Data');

    $.ajax({
      type: "POST",
      url: url,
      contentType: 'application/json',
      data: JSON.stringify({}),
      dataType: 'json'
  }).done(function(data) {
      //prioritiesMat = data['newRes']
      console.log(data)
      snake = constructMatrix(data['newRes'])
      relationmatrix = data['total']
      //console.log(snake)
        calcGradient(snake)
  });
}

function comparePpl(person1, person2) {
    return relationmatrix[person1][person2]
}

function initializeMatrix(r,c) {
    var x = new Array(r);
    for (var i = 0; i < x.length; i++) {
      x[i] = new Array(c);
    }
    return x;
}

function constructMatrix(data) {
    rows = 6
    cols = 25

    mat = initializeMatrix(rows, cols)
    count = 0
    for(var j = 0; j < cols - 2;j+=2 ) {
        for(var i = 0; i < rows; i++) {
            mat[i][j] = data[count];
            count++;
        }
        for(var i = rows - 1; i >= 0; i--) {
            mat[i][j + 1] = data[count];
            count++;
        }
    }
    return mat;
}

function calcGradient(snake) {
    console.log(snake.length, snake[0].length)
    for(var i = 0; i < snake.length; i++) {
        for(var j = 0; j < snake[0].length;j++) {
            var accumulate = 0
            var neighbors = 0

            if(i - 1 >= 0 && !(typeof snake[i][j] == 'undefined' || typeof snake[i-1][j] == 'undefined')) {
                accumulate += comparePpl(snake[i][j], snake[i-1][j])
                neighbors+=1
            }
            if(i + 1 < snake.length && !(typeof snake[i][j] == 'undefined' || typeof snake[i+1][j] == 'undefined')) {
                accumulate += comparePpl(snake[i][j], snake[i+1][j])
                neighbors+=1
            }
            if( j - 1 >= 0 && !(typeof snake[i][j] == 'undefined' || typeof snake[i][j - 1] == 'undefined')) {
                accumulate += comparePpl(snake[i][j], snake[i][j -1])
                neighbors+=1
            }
            if(j + 1 < snake[0].length && !(typeof snake[i][j] == 'undefined' || typeof snake[i][j + 1] == 'undefined')) {
                accumulate += comparePpl(snake[i][j], snake[i][j+1])
                neighbors+=1
            }
            console.log(accumulate/neighbors)
            var score = 255*(accumulate/neighbors)/42 // 0 - 42

            //score = 255*
            document.getElementById('r' + String(i) + 'c' + String(j)).style.background = 'rgb(' + score + ',' + score + ',' + score + ')'
        }
    }
}

function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

function baseCase() {
    var ar = new Array(148)
    for(var i = 0; i < ar.length;i++) {
        ar[i] = i;
    }
    ar = shuffle(ar);
    snakeBase = constructMatrix(ar)
}
