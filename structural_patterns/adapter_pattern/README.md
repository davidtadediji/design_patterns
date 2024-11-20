# Adapter Pattern

## What it is
The Adapter pattern allows incompatible interfaces to work together by converting one interface into another that a client expects. It acts as a bridge between two incompatible interfaces.

## How it works
The adapter converts the interface of a class into another interface that a client expects. The adapter class implements the target interface and delegates the work to an instance of the adaptee class, which has the incompatible interface.

## Why it works
It works because it provides a way to reuse existing classes that were designed with different interfaces. Instead of modifying those classes, we use an adapter to make them compatible with the system’s requirements.

## Where it is used:
- Integrating new components with legacy systems.
- Adapting third-party libraries to your system's expectations.
- When you need to use a class, but its interface doesn't match what you need.

## Advantages:
- Enables code reusability.
- Helps to integrate classes with incompatible interfaces.
- Keeps the existing codebase unchanged, promoting backward compatibility.
