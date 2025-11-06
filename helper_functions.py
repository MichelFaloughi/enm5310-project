import aurora

# Function to pretty print a Batch object
def pretty_print_batch(batch: aurora.batch.Batch) -> str:
    s = [f"Batch: {len(batch.surf_vars)} surf, {len(batch.static_vars)} static, {len(batch.atmos_vars)} atmos \n"]
    s.append(f"  Spatial shape: {batch.spatial_shape}")
    s.append(f"  Time: {batch.metadata.time}")
    s.append(f"  Levels: {batch.metadata.atmos_levels}")
    return "\n".join(s)
