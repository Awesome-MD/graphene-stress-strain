# graphene-stress-strain
lammps - simulation of a graphene sheet (with Tersoff potential) to extract stress-strain curve

### files:
* `generate_graphene.md` : how to generate graphene sheet with `VMD`
* `graphene.data` : file input for carbon atoms (generated with `VMD`)
* `graphene_relaxed.lmp` : simulation of the sheet and relaxation
* `graphene_stress_strain_deformed.lmp` : further apply deformation to generate required data for post processing
* `post-processing/stress-graph.py` : specific for this simulation to read the `log.lammps` and generate curve

(video captured with `VMD` with `DynamicBonds` and `VDW` representation)

### media:
this is the result of this simulation (as we use [`tersoff`](https://docs.lammps.org/pair_tersoff.html) potential here)
| result |expected |
|----|-----|
| <img src="media/Figure_1.png" alt="sress-strain-curve" width="600" height="418"/> | <img src="https://github.com/Awesome-MD/graphene-stress-strain/assets/26030553/6fa9c106-3177-4fdd-a750-8024e6e0c5f9" width="600" height="400"/>  taken from [here](https://journals.sagepub.com/doi/full/10.1177/18479804221110023) |


and here is the breakdown moment:

https://github.com/Awesome-MD/graphene-stress-strain/assets/26030553/71a6b6d6-edec-4bc7-819b-d744ae40fc30

<video src="media/simplescreenrecorder-2023-10-06_02.09.21.mp4" controls>
