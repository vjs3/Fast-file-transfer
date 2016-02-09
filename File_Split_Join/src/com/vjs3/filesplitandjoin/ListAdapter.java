package com.vjs3.filesplitandjoin;

import java.lang.ref.WeakReference;
import java.util.ArrayList;

import android.content.Context;
import android.content.res.Resources;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.os.AsyncTask;
import android.support.v4.util.LruCache;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewGroup.LayoutParams;
import android.widget.BaseAdapter;
import android.widget.GridView;
import android.widget.ImageView;

public class ListAdapter extends BaseAdapter {

	Context context;
	ArrayList<String> items;
	private LruCache<String, Bitmap> mMemoryCache;

	public ListAdapter(Context context, ArrayList<String> items) {
		this.context = context;
		this.items = items;

		// Get memory class of this device, exceeding this amount will throw an
		// OutOfMemory exception.
		final int maxMemory = (int) (Runtime.getRuntime().maxMemory() / 1024);

		// Use 1/8th of the available memory for this memory cache.
		final int cacheSize = maxMemory / 8;

		mMemoryCache = new LruCache<String, Bitmap>(cacheSize) {

			/*protected int sizeOf(String key, Bitmap bitmap) {
				// The cache size will be measured in bytes rather than number
				// of items.
				//return bitmap.getByteCount();
			}*/

		};
	}

	@Override
	public int getCount() {
		return items.size();
	}

	@Override
	public Object getItem(int arg0) {
		return items.get(arg0);
	}

	@Override
	public long getItemId(int arg0) {
		return arg0;
	}

	@Override
	public View getView(int arg0, View arg1, ViewGroup arg2) {
		
		return null;
	}


	/*public View getView(int arg0, View convertView, ViewGroup arg2) {
		ImageView img = null;

		if (convertView == null) {
			img = new ImageView(context);
			img.setScaleType(ImageView.ScaleType.CENTER_CROP);
			img.setLayoutParams(new GridView.LayoutParams(
					LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT));
		} else {
			img = (ImageView) convertView;
		}

		int resId = context.getResources().getIdentifier(items.get(arg0),
				"drawable", context.getPackageName());

		loadBitmap(resId, img);

		return img;
	}

	
}*/
}
