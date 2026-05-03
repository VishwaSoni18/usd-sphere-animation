from pxr import Usd, UsdGeom, Gf

# Create a new USD stage
stage = Usd.Stage.CreateNew("C:/Users/nimus/Desktop/moving_sphere.usda")

# Create sphere
sphere = UsdGeom.Sphere.Define(stage, "/World/Sphere")
sphere.CreateRadiusAttr(1.0)

# Make it transformable
xform = UsdGeom.Xformable(sphere)

# Add transform ops
translate = xform.AddTranslateOp()
scale = xform.AddScaleOp()

# ---------------------------
# 🎬 Animation (timeSamples)
# ---------------------------

# Position animation (bounce)
translate.Set(Gf.Vec3f(0, 0, 0), time=0)      # start
translate.Set(Gf.Vec3f(0, 5, 0), time=24)     # up
translate.Set(Gf.Vec3f(0, 0, 0), time=48)     # down

# Scale animation (optional but looks cool)
scale.Set(Gf.Vec3f(1, 1, 1), time=0)
scale.Set(Gf.Vec3f(1.5, 1.5, 1.5), time=24)
scale.Set(Gf.Vec3f(1, 1, 1), time=48)

# ---------------------------
# Timeline settings
# ---------------------------
stage.SetStartTimeCode(0)
stage.SetEndTimeCode(48)
stage.SetTimeCodesPerSecond(24)

# Save the file
stage.GetRootLayer().Save()

print("🎬 Moving sphere animation created successfully!")