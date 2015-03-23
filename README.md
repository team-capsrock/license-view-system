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

## 더 필요한 내용이 생기면 나중에 추가 하기 바람.
- 최초 작성일 : 2015/03/23, 작성자 : 오아람
- 수정일 : 
