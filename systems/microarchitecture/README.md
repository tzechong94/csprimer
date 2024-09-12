# notes

## moving beyond fetch, decode, execute model

### Pipelining

No longer run instructions through single cycle. In reality, pipelining is done. More efficient to design CPU in a way where instructions effectively move through CPU like they would in a factory.

- stages, progressive evaluation of instructions
- while one instruction is being decoded, next one can be fetched etc. independent.
- around 20 pipeline stage in intel cpus
- initial latency is around 15 to 20 cpu cycles.
  - for a branch instruction to be fully evaluated. cost of pipelining
- Branch prediction / speculative executive. Guess the outcome of that final evaluation through the pipeline of the branch instruction. Speculatively executive the next instruction.

  - may be right, may be wrong. has a buffer of pending results. if right, yay, if wrong, need to flush the partial results.
  - branch predictor.

- Improve clock speed, better utilize CPU

#### Instruction fetching

- batched ~16 bytes
- pre-fetching and pre populating L1 cache with these instructions.

#### Machine code instructions are decoded to micro Ops

- internal language to CPU. machine code is sth like API to CPU. there is a micro operations translation layer.
- can do things like instruction fusing. mutiple ops but we treat as one because they ahve the same logical outcome.

#### Out of order execution

#### numerous execution units, organized into ports.

- whole bunch of execution units, in the execution engine, including ALUs.
- throughput of up to 4.

#### register renaming

- modern cpu has a lot more physical registers, skylake ~180 integer registers and 168 vector registers
- renaming and store in different registers to do out of order execution/parallel computing

#### SIMD registers (single instruction multiple data)

- registers can be up to 512bits instead of 64.
- 16 of 32 bits integer, can fit into the register.
- can do pairwise vector operations with 2 of these registers.
- 