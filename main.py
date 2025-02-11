import sea_level_predictor

# Generate and save the sea level prediction plot
ax = sea_level_predictor.draw_plot()
plt.savefig("sea_level_plot.png")

print("Plot saved successfully.")
