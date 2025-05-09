# Exercise: Introduction to Rust

Now that you've learned about Rust and run your first program, it's time to practice!

## Exercise 1: Modify the Welcome Program

1. Open the `welcome.rs` file and add:

    - Your name as the author in a comment at the top
    - An additional line that displays the current date (you can hardcode this for now)
    - A line that prints "I'm excited to learn Rust for audio programming!"

2. Compile and run your modified program.

## Exercise 2: Explore Cargo

Cargo is Rust's build system and package manager. Let's create a new project with Cargo:

1. In your terminal, navigate to this module's directory.
2. Run: `cargo new hello_synth`
3. Explore the created directory structure.
4. Open `hello_synth/src/main.rs` and modify it to print the welcome message.
5. Run the program with `cargo run` from within the `hello_synth` directory.

You can use the solution by copying it to a new directory called `hello_synth`:

```bash
cp -r solution hello_synth && cd hello_synth
cargo run
```

## Questions to Consider

1. What are three key benefits of using Rust for audio programming?
2. How does Rust's approach to memory management differ from languages like C++ or Java?
3. What is the purpose of Cargo, and how does it make Rust development easier?

## Next Steps

Once you've completed these exercises, move on to Module 2 to learn about Rust's basic syntax and program structure.
