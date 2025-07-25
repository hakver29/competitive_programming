# Competitive Programming

Framework and solutions to various programming challenges on different online platforms. The aim is to create a plug-and-play setup for solving programming challenges in any language of choice.


## Project structure 

Each online platform has folders with programming solutions in each programming language.

```markdown
- [Platform1]
    - [Language1]
    - [Language2]
    - [Language3]
- [Platform2]
    ...
```

<details>
<summary>Rust</summary>
Add the rust-folder to the online platform folder by writing

```sh
cargo new rust vcs=none
```

The solution can be tested by writing 
```sh
cargo test
```
</details>


<details>
<summary>Haskell</summary>
Run 

```sh
brew install ghc
```

The solution can then be tested by writing
```sh
runhaskell your_solution.hs
```

</details>
