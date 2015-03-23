# license-view-system

Git을 통해서 모든 코드의 버전관리가 되니까, Git 사용법을 모두들 익히도록 하자.

## Coding style

- Coding style은 Google Code style에 따른다. 아래에는 Coding style을 위한 Guide Page

  [C++을 위한 Coding style guide](https://google-styleguide.googlecode.com/svn/trunk/cppguide.html)

  [Python을 위한 Coding style guid](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html)



- 또한 모든 Source code에는 Comment를 쓰고, Comment는 Doxygen의 문법에 따라 작성한다.

  [Doxygen Download link](http://sourceforge.net/projects/doxygen/)

  [Doxygen menual](http://www.stack.nl/~dimitri/doxygen/manual/index.html)

- 추가로 Package Comment 작성 규칙, Class comment 작성 규칙, Function comment 작성 규칙 등은 이후에 정리해서 다시 올리도록 함.


## Directory Tree

Directory는 Main에 두개를 만든다. 

1. __/Doc__
  여기에는 이 프로젝트를 위한 각종 문서를 업로드 한다. 
  - User menual
  - Project documents
  - Doxygen documents

2. __/Src__
  여기에는 실제 작성된 Source code들을 업로드 한다.
  - __./Server__
    Python으로 작성된 사용자 인증을 처리하는 Web server 코드를 위한 Directory
  - __./Client__
    C++로 작성된 server로 사용자 인증을 요청하는 client 코드를 위한 Dirctory

## Commit Rule

Comit/Push는 두가지 경우에 하도록 한다.
1. 하나의 연속된 작업이 끝났을 때. 

  코드 작성 중에 다른 일이 생겨서(수업을 들으러 가거나, 친구를 만나러 가는 등) 하던 일을 멈춰야 할 때는 완성이 안되더라도 꼭 Commit/Push를 해놓는다. 다만 이럴 때는 Branch를 만들어서 Commit을 해놓도록 하고, master branch는 항상 실행이 가능한 코드가 있도록 유지한다.

2. 하나의 기능이 완성되었을 때.

  연속해서 작업을 하는 도중이라도 목표로 한 기능이 하나 완성된다면 꼭 Commit을 하도록 한다. 물론 이럴 때도 master branch는 항상 실행이 가능한 코드가 있도록 유지해야 하며, 여러 기능이 묶여서 하나의 기능을 이루는 경우에는 여러 기능을 만들 때는 branch를 만들어서 매번 Commit을 하고, 하나의 큰 기능을 완성하고나면 master branch에 Commit/Push를 하도록 하자.
  
## 더 필요한 내용이 생기면 나중에 추가 하기 바람.
