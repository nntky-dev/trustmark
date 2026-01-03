1,Read Me
# TrustMark v0

TrustMark is a prototype system for recording authorship claims of AI-generated content.

This project does NOT prevent misuse or copying.
It simply records who claimed authorship and when, and allows later verification.

## What it does
- Records the creator name and timestamp for a given text
- Allows verification of identical content later
- Works as a local CLI tool and as a Web API

## What it does NOT do
- Does not prevent unauthorized reuse or screenshots
- Does not guarantee legal ownership
- Does not take responsibility for data loss

## API Endpoints

### POST /register
Registers a text with a creator name.

### POST /verify
Verifies whether the same text has been registered before.

## Status
This is an early prototype (v0) under active development.

