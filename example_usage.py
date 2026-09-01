from client import DynamicAspectRatioVisualPatchTokenizerClient

def main():
    client = DynamicAspectRatioVisualPatchTokenizerClient()
    res = client.tokenize_visual_patches(1920, 1080)
    print('Visual Patch Tokenizer: ' + res['tokenization_id'] + ' (' + res['original_resolution'] + ')')
    print('Patches: ' + str(res['patches_generated_count']) + ' | 2D RoPE: ' + str(res['2d_rope_spatial_coordinates_assigned']))
    print('Compression Ratio: ' + str(res['token_compression_ratio']) + 'x')

if __name__ == '__main__':
    main()
