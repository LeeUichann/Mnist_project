# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I4ghfTeYrSMYb92YgRpO2WhKjQMzOj3S
"""

# import some packages you need here
import torch.optim as opt
from dataset import Mnist
from model import LeNet5, CustomMLP

def train(model, trn_loader,tst_loader ,device, criterion, optimizer,tr):
    """ Train function

    Args:
        model: network
        trn_loader: torch.utils.data.DataLoader instance for training
        tst_loader: torch.utils.data.DataLoader instance for val
        device: device for computing, cpu or gpu
        criterion: cost function
        optimizer: optimization method, refer to torch.optim
        tr: threshold
    Returns:
        trn_loss: average loss value
        acc: accuracy
        val_loss: aval avg loss
        vla_acc : accuracy
    """


    trn_loss_ls, trn_acc_ls = [], []
    val_loss_ls, val_acc_ls = [], []



    epochs = 20



    for epoch in range(0,epochs):
        model.train()
        trn_loss = 0
        for img, label in trn_loader:

            optimizer.zero_grad()

            img, label = img.to(device), label.to(device)

            output = model(img)

            loss = criterion(output, label)



            trn_loss += loss.item() * img.size(0)
            loss.backward()
            optimizer.step()
            epoch_loss = trn_loss / len(trn_loader.dataset)
        trn_loss_ls.append(epoch_loss)

        val_epoch_loss = test(model,tst_loader, device,criterion)
        val_loss_ls.append(val_epoch_loss)


        if epoch % tr == (tr - 1):

            train_acc = get_accuracy(model, trn_loader, device=device)
            trn_acc_ls.append(train_acc)
            val_acc = get_accuracy(model, tst_loader, device=device)
            val_acc_ls.append(val_acc)
            print(f"epoch: {epoch} "
                  f"Train_loss: {epoch_loss:.4f}\t"
                  f"val_loss: {val_epoch_loss:.4f}\t"
                  f"Train_acc: {100*train_acc:.2f}%\t"
                  f"val_acc: {100*val_acc:.2f}%")

    get_plot(trn_loss_ls, trn_acc_ls,val_loss_ls,val_acc_ls)
    return epoch_loss,val_epoch_loss,train_acc,val_acc

def test(model, tst_loader, device, criterion):
    """ Test function

    Args:
        model: network
        tst_loader: torch.utils.data.DataLoader instance for testing
        device: device for computing, cpu or gpu
        criterion: cost function

    Returns:
        val_epoch_loss: average loss value

    """

    model.eval()

    tst_loss = 0

    with torch.no_grad():

        for img, label in tst_loader:

            img, label = img.to(device), label.to(device)

            output = model(img)

            loss = criterion(output, label)

            tst_loss += loss.item() * img.size(0)



    val_epoch_loss = tst_loss / len(tst_loader.dataset)

    return val_epoch_loss


def get_accuracy(model, data_loader, device):

    """
    Args:
        model: LeNet5 or CustomMLP
        data_loader: data_loader
        device: device

    Return:
        correct / n
    """
    correct = 0
    n = 0
    with torch.no_grad():
      model.eval()
      for img, label in data_loader:
          img, label = img.to(device), label.to(device)

          y_pre = model(img)


          _,pred_label = torch.max(y_pre,1)


          n += label.size(0)
          correct += (pred_label==label).sum().item()

    return correct / n

def get_plot(trn_loss_ls, trn_acc_ls,val_loss_ls,val_acc_ls):
    """ get Plot

    Args:
        trn_loss_ls: list of training losses per epoch
        trn_acc_ls: list of training accuracy per epoch
        val_loss_ls: list of val losses per epoch
        val_acc_ls: list of val losses per epoch
    """
    epochs = range(1, len(trn_loss_ls) + 1)

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(epochs, trn_loss_ls, 'b', label='Training Loss')
    plt.plot(epochs, val_loss_ls, 'r', label='Validation Loss')
    plt.title('Training Loss and val Loss per Epoch')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(epochs, trn_acc_ls, 'b',label='Training acc')
    plt.plot(epochs, val_acc_ls, 'r', label = 'Validation acc')
    plt.title('Training Accuracy and val Accuracy per Epoch')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    """ Main function

        Here, you should instantiate
        1) Dataset objects for training and test datasets
        2) DataLoaders for training and testing
        3) model
        4) optimizer: SGD with initial learning rate 0.01 and momentum 0.9
        5) cost function: use torch.nn.CrossEntropyLoss

    """
    file_path_tr = '../file_path/train.tar'
    file_path_tst = '../file_path/test.tar'

    # Image resize and normalization[0,1]
    transform = transforms.Compose([
        transforms.Resize((32,32)),
        transforms.ToTensor()
    ])

    # get train, test dataset
    train_dataset = Mnist(file_path=file_path_tr, transform = transform)
    test_dataset = Mnist(file_path=file_path_tst, transform = transform)

    # get train,test loader dataset
    trn_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    tst_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)


    device = torch.device('cuda' if torch.cuda.is_available else 'cpu')
    criterion = nn.CrossEntropyLoss()


    # LeNet5
    model1 = LeNet5()
    optimizer = opt.SGD(model1.parameters(),lr = 0.01, momentum = 0.9)
    model1.to(device)
    trn_loss_ls, acc_ls,val_loss_ls,val_acc_ls = train(model1,trn_loader,tst_loader,device,criterion, optimizer,tr=1)

    # CustomMLP
    model2 = customMLP()
    model2.to(device)
    optimizer = opt.SGD(model2.parameters(),lr = 0.01, momentum = 0.9)
    trn_loss_ls, acc_ls,val_loss_ls,val_acc_ls = train(model2,trn_loader,tst_loader,device,criterion, optimizer,tr=1)









if __name__ == '__main__':
    main()