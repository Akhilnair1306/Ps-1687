import React from 'react';

function CardInfo() {
  return (
    <div className="mt-20 ml-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-40">
      <div className="p-7 border border-black rounded-lg flex items-center justify-between">
        <div>
          <h2 className="font-semibold">Total Tweets Scraped</h2>
          <h2>2</h2>
        </div>
      </div>
      <div className="p-7 border border-black rounded-lg flex items-center justify-between">
        <div>
          <h2 className="font-semibold">Total Disastrous Tweets</h2>
          <h2>2</h2>
        </div>
      </div>
      <div className="p-7 border border-black rounded-lg flex items-center justify-between">
        <div>
          <h2 className="font-semibold">Total Non-Disastrous Tweets</h2>
          <h2>2</h2>
        </div>
      </div>
    </div>
  );
}

export default CardInfo;
