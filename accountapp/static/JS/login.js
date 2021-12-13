function send_input() {
    axios.post('/accounts/login/', {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
      })
      .then(function (response) {
        // 성공했을 경우
        console.log(response);

        document.getElementById('alert_box').innerHTML
                 += "<div class='btn btn-primary rounded-pill px-5 mb-3'>로그인을 성공했습니다. </div>";

        // Token 수령 후 쿠키 생성
        document.cookie = "drf_token=Token " + response.data['token'];

//        window.location.href = '/accounts/hello_world_template/';

      })
      .catch(function (error) {
        // 실패했을 경우
        console.log(error);

        document.getElementById('alert_box').innerHTML
                 += "<div class='btn btn-danger rounded-pill px-5 mb-3'>로그인을 실패했습니다. </div>";
      });
}
