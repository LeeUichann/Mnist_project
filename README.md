1. LeNet5 model과 Custom MLP model의 총 파라미터 개수 비교

1.1 **LeNet5:** 

convolution layer(커널 크기 x 입력 채널 수 x 출력 채널 수 + 출력 채널 수의 bias)
fully connected layer(입력 노드 수 x 출력 노드 수 + 출력 노드 수의 bias)
batchnorm(입력 채널 수 x 2)

총 파라미터 수 = convolution layer + fully connected layer + batchnorm layer

즉, 구현한 LeNet5 model의 총 파라미터 개수는 **61990개** 

1.2 **custom MLP:**

fully connected layer(입력 노드 수 x출력 노드 수 + 출력 노드 수의 bias)

구현한 custom MLP의 총 파라미터 수는 **62110개**


2. LeNet5, custom MLP의 loss, acc plot

2.1 **LeNet5**

<img width="819" alt="lenet" src="https://github.com/LeeUichann/Mnist_project/assets/166983272/e82e3eef-2f1f-48cd-aa98-e42fa847e65b"><br/><br/>


<img width="887" alt="lenet_plot" src="https://github.com/LeeUichann/Mnist_project/assets/166983272/d3ec9758-fd81-4c41-8a65-117465a241b8">

2.2 **custom MLP**

<img width="725" alt="mlp" src="https://github.com/LeeUichann/Mnist_project/assets/166983272/c8add724-ebdb-4156-ab67-1898140c13c0"><br/><br/>

<img width="887" alt="mlp_plot" src="https://github.com/LeeUichann/Mnist_project/assets/166983272/2848deec-2907-40c8-856d-9688ab93b8bc">

plot을 보면 LeNet5가 train Loss 및 validation loss가 더 빨리 떨어지는 것을 볼 수 있으며 validation accuracy 지표 또한 custom MLP보다 높은 것을 볼 수 있다.

즉, 구현한 LeNet5의 accuracy는 논문의 accuracy와 비슷했고 custom MLP보다 성능이 좋다고 볼 수 있다.


3. LeNet5 regularization

본 구현에서 LeNet 성능을 올리기위해 batchnormalization과 dropout을 사용했다.

batchnorm과 dropout의 효과를 검증하기 위해 regularization 기법을 사용하지 않은 LeNet model의 loss와 accuracy를 plot

<img width="723" alt="스크린샷 2024-04-15 오후 7 23 35" src="https://github.com/LeeUichann/Mnist_project/assets/166983272/b91bfde5-9bed-44e0-aac7-6260d4e1ef78"><br/><br/>

<img width="888" alt="스크린샷 2024-04-15 오후 7 23 48" src="https://github.com/LeeUichann/Mnist_project/assets/166983272/9ff9e5d4-3c87-4a58-9bcc-38742ae2bdff">

앞서 본 regularization을 사용한 LeNet model보다 accuracy가 안 좋은 것을 볼 수 있었고 validation loss가 더 빨리 상승하는 것을 볼 수 있다.

즉, batchnorm과 dropout이 LeNet model을 overfitting 문제를 완화시키며 성능이 더 좋은 것을 확인할 수 있었다.
