1. LeNet5 model과 Custom MLP model의 총 파라미터 개수 비교

1.1 **LeNet5:** 

convolution layer(커널 크기 x 입력 채널 수 x 출력 채널 수 + 출력 채널 수의 bias)
fully connected layer(입력 노드 수 x 출력 노드 수 + 출력 노드 수의 bias)
batchnorm(입력 채널 수 x 2)

총 파라미터 수 = convolution layer + fully connected layer + batchnorm layer

즉, LeNet5 model의 총 파라미터 개수는 **61990개** 

1.2 **custom MLP:**

fully connected layer(입력 노드 수 x출력 노드 수 + 출력 노드 수의 bias)

custom MLP의 총 파라미터 수는 **62110개**


2. LeNet5, custom MLP의 loss, acc plot
3. 
