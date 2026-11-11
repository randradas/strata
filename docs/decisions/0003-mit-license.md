# 0003. MIT license, generated files belong to the user

Status: accepted
Date: 2026-11-11

strata is MIT licensed (spec 007). `strata init` copies shipped templates into user repos, and MIT's
notice clause could be read as making users keep strata's notice in their own `CLAUDE.md` and docs.
So a separate statement, `LICENSE-GENERATED.md`, gives generated files to the user with no notice;
the `LICENSE` file stays standard MIT so GitHub and PyPI detect it. Text adapted from others (the
grill skill) keeps its own license.

## Considered options

- Apache-2.0: patent grant, but longer, a NOTICE file, and little value for a small CLI.
- GPL: copyleft on templates copied into user repos would scare users off.
- MIT-0 for templates only: no notice needed, but two licenses in one package.
- Editing the MIT text to add the exception: tools stop detecting it as MIT.

## Consequences

- Changing the license later needs every contributor's consent; keep contributions under MIT.
- New adapted third-party text must ship its own license file and be named in `LICENSE-GENERATED.md`.
